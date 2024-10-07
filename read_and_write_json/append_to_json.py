import os
import json
from read_and_write_json.write_data_to_file import write_data_to_file

def append_to_json_file(file_path, new_data):
    if os.path.exists(file_path):
        # File exists, read and append data
        try:
            with open(file_path, "r+") as file:
                data = json.load(file)
                # Ensure the file contains a dictionary
                if isinstance(data, dict):
                    if 'comments' in data:
                        data['comments'].append(new_data)
                        print("comments in data")
                    else:
                        data['comments'] = []
                        data['comments'].append(new_data)
                        print("comments not in data")
                else:
                    data = {}
                    data['comments'] = []
                    data['comments'].append(new_data)
                    print("JSON content is not a dictionary.")
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
        except json.JSONDecodeError:
            print("JSONDecodeError @ append_to_json_file")
            # Handle case where file is empty or invalid JSON
            data = {}
            data['comments'] = []
            data['comments'].append(new_data)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            #write_data_to_file("errorMessageReadComments.json", f"Error reading JSON file Exception @ append_to_json_file{file_path}")
        except Exception as e:
            print("Exception @ append_to_json_file")
            data = {}
            data['comments'] = []
            data['comments'].append(new_data)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            #write_data_to_file("errorMessageReadComments.json", f"Error reading JSON file Exception @ append_to_json_file {file_path}: {e}")

                
            # Move to the beginning and truncate to overwrite
    else:
        # File does not exist, create and write data
        print("file_path is ",file_path)
        with open(file_path, "w") as file:
            data = {}
            data['comments'] = []
            data['comments'].append(new_data)
            json.dump(data, file, indent=4)
            #write_data_to_file("errorMessageReadComments.json", f" Error reading JSON file @os.path.exists(file_path):  {file_path}: {e}")