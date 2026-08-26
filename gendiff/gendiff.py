from gendiff.parser import parse_file
from gendiff.diff_tree import build_diff_tree
from gendiff.formatters.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    
    raise ValueError(f"Unknown format: {format_name}")

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)

    raise ValueError(f"Formato no soportado: {format_name}")
