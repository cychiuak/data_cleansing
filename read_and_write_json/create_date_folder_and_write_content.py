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
        new_json_file_path = os.path.join(summary_folder_path, f"summary")
        with open(new_json_file_path, 'w') as new_json_file:
            articles = {}
            articles['articles'] = []
            articles['articles'].append(article_content)
            json.dump(articles, new_json_file, indent=4)
            print(f"Written JSON object to: {new_json_file_path}")
    else:
        new_json_file_path = os.path.join(summary_folder_path, f"summary")
        try:
            with open(new_json_file_path, 'r+') as file:
                data = json.load(file)
                # Ensure the file contains a dictionary
                print("data is ",data)
                if isinstance(data, dict):
                    if 'articles' in data:
                        print("data['comments'] is ",data['articles'])
                        data['articles'].append(article_content)
                        print("comments in data")
                    else:
                        data['articles'] = []
                        data['articles'].append(article_content)
                        print("comments not in data")
                else:
                    print("JSON content is not a dictionary.")
                    return
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
        except Exception as e:
            with open(new_json_file_path, "w") as file:
            # Handle case where file is empty or invalid JSON
                data['articles'] = []
                data['articles'].append(article_content)
                json.dump(data, file, indent=4)
                
            # Move to the beginning and truncate to overwrite
