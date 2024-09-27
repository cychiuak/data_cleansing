import os
import json
from collections import defaultdict
from helper_function import write_data_to_file

def count_companies_in_json_files(base_folder_path,file_range):
    company_count = defaultdict(int)
    # i = 10
    number_of_empty_primary_ticker = 0
    empty_primary_ticker = []
    total_files = 0
    is_empty_primarty_ticker = False
    for num_folder in range(1, file_range):
      print("num_folder is ",num_folder) 
      folder_path = f"{base_folder_path}/folder_{num_folder}"
      for filename in os.listdir(folder_path):
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
                      data_tag = data['data']['relationships']['secondaryTickers']['data'][0]['id']
                      number_of_empty_primary_ticker += 1
                      empty_primary_ticker.append(file_path)
                      is_empty_primarty_ticker = True
                    print("data_tag is ",data_tag) 
                    print("\n")
                    data_included = data['included']
                    # print("data_included is ",data_included)
                    # print("\n")
                    company_name = ''
                    for j in range(len(data_included)):
                        try:
                            if data_included[j]['id'] == data_tag:
                                company_name = data_included[j]['attributes']['company']
                                print("company is ",company_name)
                                print("\n")
                              
                                if company_name:
                                  company_count[company_name] += 1
                                j += 1
                        except:
                            print("Error")
                            company_count['Error_in finding_company_name'] += 1
                    i += 1
                    if company_name == '':
                      print("company_name is empty")
                      print("\n")
                      company_count['Error_empty_company_name'] += 1
                    if is_empty_primarty_ticker:
                      write_data_to_file.write_data_to_file("no_primary_ticker.json", company_name)
                      is_empty_primarty_ticker = False
                  except:
                      company_count['Error_any'] += 1
                      print("Error")
          # print("i is ",i)
                      
          # if i > 15:
          #     i = 10
          #     break
    print("number_of_empty_primary_ticker is ",number_of_empty_primary_ticker)
    print("empty_primary_ticker is ",empty_primary_ticker)
    company_count['total_files'] = total_files
    return dict(company_count)