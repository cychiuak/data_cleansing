import os
import json
from collections import defaultdict
from read_and_write_json import write_data_to_file
from read_and_write_json.move_json_to_company_folder import move_json_to_company_folder
from datetime import datetime, timedelta
from read_and_write_json.load_and_move_and_extract_file import load_and_move_and_extract_file
from read_and_write_json.clean_html import clean_html

def count_companies_in_json_files(initial_folder_number, end_folder_number, base_folder_path,destination_directory,comments_directory):
    company_count = defaultdict(int)
    # i = 10
    number_of_empty_primary_ticker = 0
    empty_primary_ticker = []
    total_files = 0
    for num_folder in range(initial_folder_number, end_folder_number):
      print("num_folder is ",num_folder) 
      folder_path = f"{base_folder_path}/folder_{num_folder}"
      for filename in os.listdir(folder_path):
          is_empty_primary_ticker = False
          total_files += 1
          if filename.endswith('.json'):
              file_path = os.path.join(folder_path, filename)
              print(file_path)
              with open(file_path, 'r') as file:
                  try:
                    data = json.load(file)
                    # print("\n")
                    # print(data)
                    # content = data['data']['relationships']
                    # print("data.relationships is ",content)
                    # print("\n")
                    # primary_ticker = data['data']['relationships']['primaryTickers']
                    # print("primaryTickers is ",primary_ticker)
                    # print("\n")
                    if data['data']['relationships']['primaryTickers']['data']:
                      data_tag = data['data']['relationships']['primaryTickers']['data'][0]['id']     
                    else:
                      print("primatyTicker is empty")
                      is_empty_primary_ticker = True
                      data_tag = data['data']['relationships']['secondaryTickers']['data'][0]['id']
                      number_of_empty_primary_ticker += 1
                      empty_primary_ticker.append(file_path)
                      company_count['number_of_empty_primary_ticker'] += 1
                    print("data_tag is ",data_tag) 
                    print("\n")
                    data_included = data['included']
                    # print("data_included is ",data_included)
                    # print("\n")
                    company_name = ''
                    company_tag = ''
                    for j in range(len(data_included)):
                        try:
                            if data_included[j]['id'] == data_tag:
                                company_name = data_included[j]['attributes']['company']
                                company_tag = data_included[j]['attributes']['name']
                                print("company is ",company_name)
                                print("tag is ",company_tag)
                                print("\n")
                              
                                if company_name:
                                  company_count[company_name] += 1
                                j += 1
                        except:
                            print("Error_in finding_company_name")
                            company_count['Error_in finding_company_name'] += 1
                    # i += 1
                    if company_name == '':
                      print("company_name is empty")
                      print("\n")
                      company_count['Error_empty_company_name'] += 1
                    if is_empty_primary_ticker:
                      company_count['is_empty_primary_ticker'] += 1
                      is_empty_primary_ticker = False
                      write_data_to_file.write_data_to_file("no_primary_ticker.json", company_name)
                    # we now have company_tag, the folderpath we want to move our files: destination_directory + company_tag
                    publish_date = data.get("data", {}).get("attributes", {}).get("publishOn", None)
                    if publish_date:
                      publish_date = datetime.fromisoformat(publish_date)
                    else:
                      write_data_to_file.write_data_to_file("errorMessage.json", "publishDateNotFoundError" + file_path)
                    # print("publish_date is ",publish_date)
                    tzinfo = publish_date.tzinfo
                    publish_date = publish_date - timedelta(hours=9, minutes=30)
                    date_str = ''
                    if publish_date and publish_date >= datetime(2020, 1, 1, tzinfo=tzinfo) and publish_date <= datetime.now(tzinfo):
                       date_str = publish_date.strftime('%Y-%m-%d')
                    else:
                       write_data_to_file.write_data_to_file("too_long_ago.json", "publish_date: " + date_str + " file_path: " + file_path)
                       continue
                    article_content = {}
                    article_content["title"] = clean_html(data['data']['attributes']['title'])
                    article_content["summary"] = clean_html(data['data']['attributes']['summary'][0]) if len(data['data']['attributes']['summary']) > 0 else []
                    article_content["content"] = clean_html(data['data']['attributes']['content'])
                    # print("destination_directory is ",destination_directory)
                    # print("file_path is ",file_path)
                    # print("company_name is ",company_name)
                    # print("filename is ",filename)
                    comments_json_file_path = os.path.join(comments_directory,filename)
                    move_json_to_company_folder(destination_directory, file_path, company_tag,filename, company_name, date_str,article_content)
                    company_folder = os.path.join(destination_directory, company_tag)
                    load_and_move_and_extract_file(comments_json_file_path, company_folder, filename)
                    
                  except Exception as e:
                      company_count['Error_any'] += 1
                      print("Error")
                      print(f"An error occurred: {e}")
                      print(e)
                      if 'data' in str(e):
                        print("data_error")
                        company_count['Empty_Data'] += 1
                      else:
                        write_data_to_file.write_data_to_file("errorMessage_2_version.json", str(e) + file_path)
          # print("i is ",i)
                      
          # if i > 15:
          #     i = 10
          #     break
    # print("number_of_empty_primary_ticker is ",number_of_empty_primary_ticker)
    # print("empty_primary_ticker is ",empty_primary_ticker)
    company_count['total_files'] = total_files
    return dict(company_count)