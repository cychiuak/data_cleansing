from sort_date.iterate_folder_and_sort_json import iterate_folders_and_sort_json

base_directory = '../sort_date_testing'
num_same_date = iterate_folders_and_sort_json(base_directory)
print(f"Total number of files with the same date: {num_same_date}")