from read_and_write_json.write_data_to_file import write_data_to_file
from read_and_write_json.testingFunction import testing
from read_and_write_json.move_json_to_company_folder import move_json_to_company_folder
company_name = "Apple Inc." 

# write_data_to_file("no_primary_ticker.json", company_name)
testing(company_name)
destination_directory = '../seeking_alpha_split_testing_company_folder'
file_path = '../seeking_alpha_split_testing_copy/folder_4/123.json'
filename = '123.json'
move_json_to_company_folder(destination_directory, file_path, company_name,filename)