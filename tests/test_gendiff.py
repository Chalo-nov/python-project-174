from gendiff.gendiff import generate_diff


def test_generate_diff():
    result = generate_diff('file1.json', 'file2.json')
    assert isinstance(result, str)
    assert '- follow: false' in result
    assert '  host: hexlet.io' in result
    assert '+ verbose: true' in result


def test_generate_diff_yaml():
    result = generate_diff('file1.yml', 'file2.yml')
    assert isinstance(result, str)
    assert '- follow: false' in result
    assert '  host: hexlet.io' in result
    assert '+ verbose: true' in result


def test_generate_diff_nested_json():
    result = generate_diff('file1_nested.json', 'file2_nested.json')
    assert isinstance(result, str)
    assert '  - setting2: 200' in result
    assert '  + setting3: null' in result


def test_generate_diff_nested_stylish():
    result = generate_diff('file1_nested.json', 'file2_nested.json', 'stylish')
    assert isinstance(result, str)
    assert '  - setting2: 200' in result
