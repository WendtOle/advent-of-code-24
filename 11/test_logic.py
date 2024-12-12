from logic import transform_stone, blink, blink_often

def test_first_rule():
    assert transform_stone(0) == [1]

def test_second_rule():
    assert transform_stone(10) == [1, 0]

def test_third_rule():
    assert transform_stone(9) == [9 * 2024]

def test_given_example():
    assert blink([125, 17]) == [253000, 1, 7]
    assert blink([253000, 1, 7]) == [253, 0, 2024, 14168]

def test_sum():
    assert blink_often([125, 17],6) == 22
    assert blink_often([125, 17],25) == 55312
