import argparse

import json


def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration"
                                                 "files and shows a difference.")

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        help="set format of output")

    args = parser.parse_args()

    first_data = read_json(args.first_file)
    second_data = read_json(args.second_file)

    # Пока просто для проверки:
    print("Первый файл", first_data)
    print("Второй файл", second_data)


if __name__ == "__main__":
    main()
