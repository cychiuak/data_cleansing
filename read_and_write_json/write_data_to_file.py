import json

def write_data_to_file(file_path, company_name):
  try:
    with open(file_path, 'r') as file:
      data = json.load(file)  # Load existing data
  except FileNotFoundError:
    data = []
  data.append(company_name)
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)  