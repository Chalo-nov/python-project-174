import json
import os
import yaml


def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == '.json':
        return json.load(open(file_path))
    elif extension in ('.yml', '.yaml'):
        return yaml.safe_load(open(file_path))
    else:
        raise ValueError(f"Formato no soportado: {extension}")
