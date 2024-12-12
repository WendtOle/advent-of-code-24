from logic import transform_stone, blink, blink_often

def test_first_rule():
    assert transform_stone((0,1)) == [(1,1)]

def test_second_rule():
    assert transform_stone((10,1)) == [(1,1), (0,1)]

def test_third_rule():
    assert transform_stone((9,1)) == [(9 * 2024,1)]

def test_given_example():
    assert blink([(125,1), (17,1)],{})[0] == [(253000,1), (1,1), (7,1)]
    assert blink([(253000,1), (1,1), (1,1)],{})[0] == [(253,1), (0,1), (2024,2)]

def test_sum():
    assert blink_often([0], 2) == 1
    assert blink_often([125, 17],6) == 22
    assert blink_often([10, 2],7) == 37
    assert blink_often([125, 17],25) == 55312
