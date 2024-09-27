import os
import shutil

def move_json_to_company_folder(destination_directory, file_path, company_name,filename):
    print("called move_json_to_company_folder")
    company_folder = os.path.join(destination_directory, company_name)
    print("company_folder is ",company_folder)
    # Create the company folder if it doesn't exist
    if not os.path.exists(company_folder):
        os.makedirs(company_folder)
        print(f"Created folder {company_folder}")
    # Move the JSON file to the company folder
    shutil.move(file_path, os.path.join(company_folder, filename))
    print(f"Moved {filename} to {company_folder}")