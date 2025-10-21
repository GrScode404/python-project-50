import os.path

from gendiff.scripts.generate_diff import generate_diff
from tests.test_generate_diff import read_file


def test_format_plain():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.json")
    file2 = os.path.join(current_dir, "test_data", "file2.json")

    expected = read_file(os.path.join(current_dir, "test_data", "expected_diff_plain.txt"))

    result = generate_diff(file1, file2, 'plain')

    assert result == expected