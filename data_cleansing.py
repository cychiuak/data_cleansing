import os
import shutil

def split_files_into_folders(source_folder, num_folders=20):
    # Create target folders if they don't exist
    target_folder = "/Users/qiujunyi/Desktop/fyp/seeking_alpha_split2"
    for i in range(num_folders):
        os.makedirs(f"{target_folder}/folder_{i+1}", exist_ok=True)
  
    # List all JSON files in the source folder
    json_files = [f for f in os.listdir(source_folder) if f.endswith('.json')]
    print("json_file[0]: ", json_files[0]) # 
    # Distribute files into folders
    for index, file_name in enumerate(json_files):
        print("index: ", index)
        print("file_name: ", file_name)
        source_path = os.path.join(source_folder, file_name)
        print("moved from: ", source_path)
        target_sub_folder = f"{target_folder}/folder_{(index % num_folders) + 1}"
        print("moved to: ", target_sub_folder)
        shutil.move(source_path, target_sub_folder)

    print(f"Distributed {len(json_files)} files into {num_folders} folders.")

# Set your source folder path here
source_folder_path = '../SeekingAlpha_231027/articles'
split_files_into_folders(source_folder_path)