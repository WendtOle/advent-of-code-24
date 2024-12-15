from main import read_input, execute_multiple_moves, enlarge_input,print_map
from get_gps_sum import get_gps_sum

def test_example():
    [input, width, moves] = read_input("./example-1.txt")
    end = execute_multiple_moves(input, moves, width)
    assert get_gps_sum(end, width) == 2028

def test_enlarged_example():
    [small_input, small_width, moves] = read_input("./example-2.txt")
    input, width = enlarge_input(small_input), small_width * 2
    print_map(input, width)
    end = execute_multiple_moves(input, moves, width)
    print_map(end, width)
    assert get_gps_sum(end, width) == 9021