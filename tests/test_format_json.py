import json
import os

from gendiff.scripts import generate_diff


def test_format_json():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.json")
    file2 = os.path.join(current_dir, "test_data", "file2.json")

    result = generate_diff(file1, file2, 'json')
    parsed = json.loads(result)

    assert isinstance(parsed, list)
    assert all('key' in node for node in parsed)
