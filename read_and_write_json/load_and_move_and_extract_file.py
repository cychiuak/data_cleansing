import os
import json
from datetime import datetime, timedelta
from read_and_write_json import write_data_to_file
from read_and_write_json.append_to_json import append_to_json_file
from read_and_write_json.clean_html import clean_html

def load_and_move_and_extract_file(comments_file_path, company_folder_path,comments_filename):
    error = 0
    try:
        with open(comments_file_path, 'r') as json_file:
            json_content = json.load(json_file)
            # print(f"Contents of {comments_file_path}: {json_content}")
            for i in range(len(json_content['data'])):
                print(f"Comment {i}: {json_content['data'][i]}")
                publish_date = json_content['data'][i]['attributes']['createdOn']
                content = clean_html(json_content['data'][i]['attributes']['content'])

                print(f"Publish date: {publish_date}")
                publish_date = datetime.fromisoformat(publish_date)
                publish_date = publish_date - timedelta(hours=9, minutes=30)
                tzinfo = publish_date.tzinfo
                if publish_date and publish_date >= datetime(2020, 1, 1, tzinfo=tzinfo) and publish_date <= datetime.now(tzinfo):
                    date_str = publish_date.strftime('%Y-%m-%d')
                    print(f"Date string: {date_str}")
                    date_folder_path = os.path.join(company_folder_path, date_str)
                    summary_folder_path = os.path.join(date_folder_path, "summary")
                    print(f"Date folder path: {date_folder_path}")
                    if not os.path.exists(date_folder_path):
                        os.makedirs(date_folder_path)
                        print(f"Created folder: {date_folder_path}")
                        os.makedirs(summary_folder_path)
                    summary_file_path = os.path.join(summary_folder_path, f"summary")
                    new_json_file_path = os.path.join(date_folder_path, f"comments_{comments_filename}")
                    existing_comments = {}
                    try:
                        with open(new_json_file_path, 'r') as file:
                            existing_comments = json.load(file)  # Load existing data
                    except FileNotFoundError:
                        existing_comments['comments'] = []
                    existing_comments['comments'].append(json_content['data'][i])
                    with open(new_json_file_path, 'w') as new_json_file:
                        json.dump(existing_comments, new_json_file, indent=4)
                        print(f"Written JSON object to: {new_json_file_path}")
                    append_to_json_file(summary_file_path, content)
                    # with open(summary_file_path, 'w') as new_json_file:
                    #     json.dump(input_content, new_json_file, indent=4)
                    #     print(f"Written JSON object to: {new_json_file_path}")

    except json.JSONDecodeError as e:
        print(f"Error reading JSON file {comments_file_path}: {e}")
        error += 1
        write_data_to_file.write_data_to_file("errorMessage.json", str(e) + comments_file_path)
    except Exception as e:
        print(f"Error reading JSON file {comments_file_path}")
        write_data_to_file.write_data_to_file("errorMessage.json", str(e) + comments_file_path)