import os
import shutil

def find_and_move_file(filename, search_directory, target_directory):
    """
    Search for a file in a directory and move it to a new directory.

    :param filename: The name of the file to search for.
    :param search_directory: The directory to search in.
    :param target_directory: The directory to move the file to.
    """
    # Walk through the search_directory
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            # Full path of the file
            file_path = os.path.join(root, filename)
            print(f"File found at: {file_path}")
            
            # Ensure target directory exists
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            
            # Full path to move the file to
            target_path = os.path.join(target_directory, filename)
            
            # Move the file
            shutil.move(file_path, target_path)
            print(f"File moved to: {target_path}")
            return
        
    # If file is not found
    print(f"File '{filename}' not found in directory '{search_directory}'.")

