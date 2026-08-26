def stringify(val, depth):
    if val is none:
        return 'none'
    if isinstance(val, bool):
        return str(val).lower()
    if not isinstance(val, dict):
        return str(val)

    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
    deep_indent = ' ' * ((depth + 1) * indent_size)

    lines = []
    for k, v in val.items():
        lines.append(f"{deep_indent}{k}: {stringify(v, depth + 1)}")

    result = '\n'.join(lines)
    return f"{{\n{result}\n{current_indent}}}"


def format_stylish(diff, depth=1):
    indent_size = 4
    indent = ' ' * (depth * indent_size - 2)
    closing_indent = ' ' * ((depth - 1) * indent_size)

    lines = []
    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'added':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}+ {key}: {val}")
        elif node_type == 'removed':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}- {key}: {val}")
        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}  {key}: {val}")
        elif node_type == 'changed':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['new_value'], depth)
            lines.append(f"{indent}- {key}: {old_val}")
            lines.append(f"{indent}+ {key}: {new_val}")
        elif node_type == 'nested':
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {children_str}")

    result = '\n'.join(lines)
    return f"{{\n{result}\n{closing_indent}}}"
