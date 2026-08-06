import json


def stringify_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    all_keys = sorted(data1.keys() | data2.keys())
    lines = []

    for key in all_keys:
        if key in data1 and key not in data2:
            val = stringify_value(data1[key])
            lines.append(f'  - {key}: {val}')
        elif key not in data1 and key in data2:
            val = stringify_value(data2[key])
            lines.append(f'  + {key}: {val}')
        elif data1[key] == data2[key]:
            val = stringify_value(data1[key])
            lines.append(f'    {key}: {val}')
        else:
            val1 = stringify_value(data1[key])
            val2 = stringify_value(data2[key])
            lines.append(f'  - {key}: {val1}')
            lines.append(f'  + {key}: {val2}')

    result = ['{'] + lines + ['}']
    return '\n'.join(result)
