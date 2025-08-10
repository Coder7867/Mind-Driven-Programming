import json
import os

def save_data(file_path, key, value):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)
    with open(file_path, 'r') as f:
        data = json.load(f)
    data[key] = value
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def load_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)
