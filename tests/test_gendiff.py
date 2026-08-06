from gendiff.gendiff import generate_diff


def test_generate_diff():
    result = generate_diff('file1.json', 'file2.json')
    assert isinstance(result, str)
    assert '- follow: false' in result
    assert '  host: hexlet.io' in result
    assert '+ verbose: true' in result