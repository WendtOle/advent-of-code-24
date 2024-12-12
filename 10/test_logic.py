from logic import get_sum, get_surrounded_positions, get_surrounded_next_level

def test_first_example():
    input = """
    0123
    1234
    8765
    9876
    """
    assert get_sum(input) == [1,16]

def test_second_example():
    input = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
    assert get_sum(input) == [36,81]

def test_position():
    assert get_surrounded_positions(4,3) == [3,5,1,7]
    assert get_surrounded_positions(3,3) == [4,0,6]

def test_get_surrounded_next_level():
    input = list(map(lambda char: int(char),"0123123487659876"))
    assert get_surrounded_next_level(0,0,input,4) == [1,4]
