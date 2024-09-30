import os
import json
from datetime import datetime
from sort_date.sort_json_files_by_date import sort_json_files_by_date

def iterate_folders_and_sort_json(base_directory):
    num_same_date = 0
    for root, dirs, files in os.walk(base_directory):
        sorted_files, num_same_date = sort_json_files_by_date(root)
        num_same_date += num_same_date
        if sorted_files:
            print(f"Sorted JSON files in {root}:")
            for file in sorted_files:
                print(f"  {file}")
    return num_same_date