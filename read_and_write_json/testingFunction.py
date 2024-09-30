import os
import json
from collections import defaultdict
from read_and_write_json import write_data_to_file

def testing(company_name):
    write_data_to_file.write_data_to_file("no_primary_ticker.json", company_name)