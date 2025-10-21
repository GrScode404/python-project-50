import os.path

import pytest

from gendiff.scripts.generate_diff import generate_diff
from tests.test_generate_diff import read_file


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.yaml")
    file2 = os.path.join(current_dir, "test_data", "file2.yaml")

    expected = read_file(os.path.join(current_dir, "test_data", "expected_diff.txt"))

    result = generate_diff(file1, file2)

    assert result.strip() == expected


def test_same_data_generate_diff():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.yaml")

    expected = read_file(os.path.join(current_dir, "test_data", "expected_diff_same.txt"))

    result = generate_diff(file1, file1)

    assert result.strip() == expected


def test_generate_diff_file_not_found():
    with pytest.raises(FileNotFoundError):
        generate_diff("no_file1.yaml", "no_file2.yaml")
