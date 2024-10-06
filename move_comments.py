from move_comments_to_correct_folder.move_comments_to_correct_folder import move_commments_to_correct_folder
from move_comments_to_correct_folder.load_and_move_file import load_and_move_file
import os
import json
from datetime import datetime, timedelta

# target_directory = '../seeking_alpha_split_testing_company_folder2'
target_directory = '../find_comments_testing'
comment_directory = '../comments2_copy/content'


# Specify the directory path
from pathlib import Path


directory_path = Path(target_directory)

# Iterate through all subfolders and files inside them
for subfolder in directory_path.iterdir():
    if subfolder.is_dir():
        print(f"Subfolder found: {subfolder}")
        company_folder_path = Path(subfolder)
        print(f"company_folder_path is ",company_folder_path)
        for date_folder in company_folder_path.iterdir():
            if date_folder.is_dir() and date_folder.name != "company_name":
                for file in date_folder.rglob('*'):
                    if file.is_file():
                        print(f"File found: {file}")
                        filename = os.path.basename(file).split('/')[-1]
                        print(f"filename is ",filename)
                        comments_json_file_path = os.path.join(comment_directory,filename)
                        print("company_folder_path is ",company_folder_path)
                        load_and_move_file(comments_json_file_path, company_folder_path, filename)
                        # try:
                        #     with open(comments_json_file_path, 'r') as json_file:
                        #         json_content = json.load(json_file)
                        #         print(f"Contents of {comments_json_file_path}: {json_content}")
                        #         for i in range(len(json_content['data'])):
                        #             print(f"Comment {i}: {json_content['data'][i]}")
                        #             publish_date = json_content['data'][i]['attributes']['createdOn']
                        #             print(f"Publish date: {publish_date}")
                        #             publish_date = datetime.fromisoformat(publish_date)
                        #             date_str = publish_date.strftime('%Y-%m-%d')
                        #             print(f"Date string: {date_str}")
                        #             date_folder_path = os.path.join(company_folder_path, date_str)
                        #             print(f"Date folder path: {date_folder_path}")
                        #             if not os.path.exists(date_folder_path):
                        #                 os.makedirs(date_folder_path)
                        #                 print(f"Created folder: {date_folder_path}")
                        #             new_json_file_path = os.path.join(date_folder_path, f"comments_{filename}")
                        #             with open(new_json_file_path, 'w') as new_json_file:
                        #                 json.dump(json_content['data'][i], new_json_file, indent=4)
                        #                 print(f"Written JSON object to: {new_json_file_path}")

                        # except json.JSONDecodeError as e:
                        #     print(f"Error reading JSON file {comments_json_file_path}: {e}")
                        # except:
                        #     print(f"Error reading JSON file {comments_json_file_path}")
