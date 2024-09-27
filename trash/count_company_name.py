import os
import json
from collections import defaultdict

def count_companies_in_json_files(folder_path):
    company_count = defaultdict(int)

    # Iterate over all JSON files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                # Get secondaryTickers IDs
                secondary_ticker_ids = [
                    item['id'] for item in data['data']['relationships']['secondaryTickers']['data']
                ]
                
                # Find company names using the IDs
                for item in data['included']:
                    if item['id'] in secondary_ticker_ids and item['type'] == 'tag':
                        company_name = item['attributes'].get('company')
                        if company_name:
                            company_count[company_name] += 1

    return dict(company_count)

# Example usage
folder_path = '../seeking_alpha_split_final/folder_1'
company_counts = count_companies_in_json_files(folder_path)
print(company_counts)