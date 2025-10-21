import os.path

import pytest

from gendiff.scripts.generate_diff import generate_diff


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read().strip()


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.json")
    file2 = os.path.join(current_dir, "test_data", "file2.json")

    expected = read_file(
        os.path.join(
            current_dir,
            "test_data",
            "expected_diff.txt"
        )
    )

    result = generate_diff(file1, file2)

    assert result.strip() == expected


def test_same_data_generate_diff():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, "test_data", "file1.json")

    expected = read_file(
        os.path.join(
            current_dir,
            "test_data",
            "expected_diff_same.txt"
        )
    )

    result = generate_diff(file1, file1)

    assert result == expected


def test_generate_diff_file_not_found():
    with pytest.raises(FileNotFoundError):
        generate_diff("no_file1.json", "no_file2.json")