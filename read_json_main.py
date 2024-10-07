import os
import json
from collections import defaultdict
from read_and_write_json.count_companies_in_json import count_companies_in_json_files
from read_and_write_json.write_counts_to_json import write_counts_to_json
import sys
sys.path.append('../helper_function')

output_file_path = 'outputTesting.json'
# folder_path = '../seeking_alpha_split_testing_copy'
# destination_directory = '../seeking_alpha_split_testing_company_folder2'
testing_folder_path = '../final_testing'
testing_destination_directory = '../final_testing_destination'

comments_directory = '../comments2_copy/content'

initial_folder_number = 1
end_folder_number = 3
# company_counts = count_companies_in_json_files(initial_folder_number, end_folder_number,folder_path,destination_directory)
company_counts = count_companies_in_json_files(initial_folder_number, end_folder_number,testing_folder_path,testing_destination_directory, comments_directory)
write_counts_to_json(company_counts, output_file_path)