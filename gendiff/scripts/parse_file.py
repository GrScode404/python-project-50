import json
import os

import yaml


def parse_file(filepath):
    _, ext = os.path.splitext(filepath)

    with open(filepath, 'r') as f:
        content = f.read()

    if ext in ['.json']:
        return json.loads(content)
    elif ext in ['.yml', '.yaml']:
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
