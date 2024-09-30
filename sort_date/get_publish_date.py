import os
import json
from datetime import datetime

def get_publish_date(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            publish_date = data.get("data", {}).get("attributes", {}).get("publishOn", None)
            return datetime.fromisoformat(publish_date) if publish_date else None
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Error reading {json_file}: {e}")
        return None