import os
import json
import shutil
from datetime import datetime
from sort_date.get_publish_date import get_publish_date

def sort_json_files_by_date(directory):
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    files_with_dates = []
    num_same_date = 0
    for json_file in json_files:
        full_path = os.path.join(directory, json_file)
        publish_date = get_publish_date(full_path)
        print("publish_date is ",publish_date)
        if publish_date:
            date_str = publish_date.strftime('%Y-%m-%d')
            print("date_str is ",date_str)
            files_with_dates.append((json_file, publish_date))
            date_directory = os.path.join(directory, date_str)

            if not os.path.exists(date_directory):
                os.makedirs(date_directory)

            shutil.move(full_path, os.path.join(date_directory, json_file))

    # Sort files by publish date
    files_with_dates.sort(key=lambda x: x[1])

    sorted_files = [file for file, _ in files_with_dates]
    return sorted_files, num_same_date