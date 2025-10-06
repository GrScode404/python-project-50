import json


def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)
    result_diff = ["{"]

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            result_diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result_diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            result_diff.append(f"    {key}: {data1[key]}")
        else:
            result_diff.append(f"  - {key}: {data1[key]}")
            result_diff.append(f"  + {key}: {data2[key]}")

    result_diff.append("}")
    return "\n".join(result_diff)
