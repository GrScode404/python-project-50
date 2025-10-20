def stringify(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")
        return f"{{\n{"\n".join(lines)}\n{indent}}}"
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_stylish(diff, depth=1):
    lines = []
    indent = '    ' * (depth - 1)
    inner_indent = '    ' * depth

    for node in diff:
        key = node['key']
        status = node['status']

        if status == 'nested':
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{inner_indent}{key}: {children}")
        elif status == 'added':
            value = stringify(node['value'], depth)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == 'removed':
            value = stringify(node['value'], depth)
            lines.append(f"{indent}  - {key}: {value}")
        elif status == 'unchanged':
            value = stringify(node['value'], depth)
            lines.append(f"{inner_indent}{key}: {value}")
        elif status == 'changed':
            old_value = stringify(node['old_value'], depth)
            new_value = stringify(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")

    result = '\n'.join(lines)
    return f"{{\n{result}\n{indent}}}"




