import json

from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.scripts.diff_builder import build_diff
from gendiff.scripts.parse_file import parse_file


def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f'Unknown format: {format_name}')