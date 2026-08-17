def stringify(val, depth):
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, str) and val.lower() == 'none':
        return 'null'
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
