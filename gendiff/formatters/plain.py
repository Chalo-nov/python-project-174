def stringify_value(val):
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    if isinstance(val, (dict, list)):
        return '[complex value]'
    if isinstance(val, str):
        return f"'{val}'"
    return str(val)


def format_plain(diff, parent_path=''):
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']
        property_path = f"{parent_path}.{key}" if parent_path else key

        if node_type == 'nested':
            child_result = format_plain(node['children'], property_path)
            if child_result:
                lines.append(child_result)
        elif node_type == 'added':
            val = stringify_value(node['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {val}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif node_type == 'changed':
            old_val = stringify_value(node['old_value'])
            new_val = stringify_value(node['new_value'])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return '\n'.join(lines)
