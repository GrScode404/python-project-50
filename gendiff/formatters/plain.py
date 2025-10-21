def format_value(value):
    if isinstance(value, dict) :
        return "[complex value]"
    elif isinstance(value, bool) :
        return str(value).lower()
    elif value is None :
        return "null"
    elif isinstance(value, str) :
        return f"'{value}'"
    else :
        return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node['key']
        property_path = f"{path}.{key}" if path else key
        status = node['status']

        if status == "added":
            value = format_value(node["value"])
            lines.append(f"Property '{property_path}' was added with value: {value}")

        elif status == "removed":
            lines.append(f"Property '{property_path}' was removed")

        elif status == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(f"Property '{property_path}' was updated. From {old_value} to {new_value}")

        elif status == "nested":
            lines.extend(format_plain(node["children"], property_path).splitlines())

    return "\n".join(lines)
