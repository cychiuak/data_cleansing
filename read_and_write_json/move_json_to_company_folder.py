import os
import shutil
import json
from read_and_write_json.create_date_folder_and_write_content import create_date_folder_and_write_content

def move_json_to_company_folder(destination_directory, file_path, company_tag,filename, company_name, date_str, article_content):
    print("called move_json_to_company_folder")
    company_folder = os.path.join(destination_directory, company_tag)
    print("company_folder is ",company_folder)
    # Create the company folder if it doesn't exist
    if not os.path.exists(company_folder):
        os.makedirs(company_folder)
        print(f"Created folder {company_folder}")
        os.makedirs(os.path.join(company_folder, "company_name"))
        os.makedirs(os.path.join(company_folder, "company_name", company_name))

    create_date_folder_and_write_content(company_folder, date_str, article_content)
        
    # Move the JSON file to the company folder
    shutil.move(file_path, os.path.join(company_folder, date_str, filename))
    print(f"Moved {filename} to {company_folder}")