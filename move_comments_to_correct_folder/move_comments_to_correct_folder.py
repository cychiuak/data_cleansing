import os
import shutil
import json

def move_commments_to_correct_folder(filename,path_to_file, target_directory):
    file_path = os.path.join(path_to_file, filename)
    try:
        with open(file_path, 'r') as json_file:
            content = json.load(json_file)
            print("content is ",content["data"])
            for i in range(len(content['data'])):
                publish_date = content['data'][i]['attributes']['publishOn']
                comment_from_an_user = content['data'][i]
                print("publish date is ",publish_date)
                print("comment from an user is ",comment_from_an_user)
                new_comment_filename = filename + "comments" + ".json"
                json_file_path = os.path.join(path_to_file, new_comment_filename)
                # with open(json_file_path, 'w') as json_file:
                #     json.dump(comment_from_an_user, json_file, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"Error opening file: {e}")


    # for root, dirs, files in os.walk(search_directory):
    #     if filename in files:
    #         # Return the full path of the file
    #         file_path = os.path.join(root, filename)
    #         try:
    #             with open(file_path, 'r') as json_file:
    #                 content = json.load(json_file)
    #                 return content
    #         except json.JSONDecodeError as e:
    #             print(f"Error reading JSON file: {e}")
    #         except Exception as e:
    #             print(f"Error opening file: {e}")
    
    # If the file was not found
    return None

