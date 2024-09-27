import os
import json
from collections import defaultdict
from helper_function.count_companies_in_json import count_companies_in_json_files
from helper_function.write_counts_to_json import write_counts_to_json
import sys
sys.path.append('../helper_function')

output_file_path = 'outputTesting.json'
# Example usage
folder_path = '../seeking_alpha_split_final'
file_range = 2
company_counts = count_companies_in_json_files(folder_path, file_range)
# print(company_counts)
write_counts_to_json(company_counts, output_file_path)