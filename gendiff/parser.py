import json
import yaml


def parse_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    raise ValueError(f"Unsupported file format: {file_path}")

def sanitize_data(data):
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(item) for item in data]
    if isinstance(data, str) and data.strip().lower() in ('none', 'null', ''):
        return None
    return data
