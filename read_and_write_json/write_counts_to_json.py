import os
import json
from collections import defaultdict
def write_counts_to_json(counts, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(counts, output_file, indent=4)