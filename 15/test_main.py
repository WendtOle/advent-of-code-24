from main import read_input, execute_multiple_moves
from get_gps_sum import get_gps_sum

def test_example():
    [input, width, moves] = read_input("./example-1.txt")
    end = execute_multiple_moves(input, moves, width)
    assert get_gps_sum(end, width) == 2028