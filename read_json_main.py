import os
import json
from collections import defaultdict
from helper_function.count_companies_in_json import count_companies_in_json_files
from helper_function.write_counts_to_json import write_counts_to_json
import sys
sys.path.append('../helper_function')

output_file_path = 'outputTesting.json'
# Example usage
folder_path = '../seeking_alpha_split_testing_copy'

initial_folder_number = 2
end_folder_number = 4
destination_directory = '../seeking_alpha_split_testing_company_folder'
company_counts = count_companies_in_json_files(initial_folder_number, end_folder_number,folder_path,destination_directory)
# print(company_counts)
write_counts_to_json(company_counts, output_file_path)