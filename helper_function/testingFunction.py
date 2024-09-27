import os
import json
from collections import defaultdict
from helper_function import write_data_to_file

def testing(company_name):
    write_data_to_file.write_data_to_file("no_primary_ticker.json", company_name)