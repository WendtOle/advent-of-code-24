from read_input import read_input_from_file


def test_read_single_value_from_file():
    assert read_input_from_file("./dummy-input.txt") == "XAMX"