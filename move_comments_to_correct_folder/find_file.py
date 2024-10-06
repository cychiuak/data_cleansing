import os

def find_file(filename, search_directory,target_directory):
    """
    Search for a file with the given filename in the directory and its subdirectories.

    :param filename: The name of the file to search for.
    :param search_directory: The directory to search in.
    :return: The full path of the file if found, otherwise None.
    """
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            # Return the full path of the file
            return os.path.join(root, filename)
    
    # If the file was not found
    return None

# Example usage
filename = "example.txt"
search_directory = "/path/to/search_directory"

file_path = find_file(filename, search_directory)

if file_path:
    print(f"File found at: {file_path}")
else:
    print(f"File '{filename}' not found in directory '{search_directory}'.")