import os
import shutil
import json

def create_date_folder_and_write_content(company_folder, date_str, article_content ):
    date_folder = os.path.join(company_folder, date_str)
    # Create the date folder if it doesn't exist
    summary_folder_path = os.path.join(date_folder, "summary")
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)
        print(f"Created folder {date_folder}")
        os.makedirs(os.path.join(date_folder, "summary"))
    summary_folder_path = os.path.join(summary_folder_path)
    new_json_file_path = os.path.join(summary_folder_path, f"summary")
    with open(new_json_file_path, 'w') as new_json_file:
        json.dump(article_content, new_json_file, indent=4)
        print(f"Written JSON object to: {new_json_file_path}")
