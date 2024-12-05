from count_at_coordinate import count_at_coordinate, next_position, Dir,count_whole_puzzle
import pytest
from read_input import read_input_from_file
from count_MAS import count_whole_puzzle as count_MAS_whole_puzzle

def test_count_at_coordinate():
    assert count_at_coordinate("XMASXXXXXXXXXXXX", 0) == 1

def test_raise_exception_for_invalid_length():
    with pytest.raises(Exception, match="invalid length"):
        count_at_coordinate("XMASS", 0)

def test_next_position_easy_right(): 
    assert next_position(0, 4, Dir.RIGHT) == 1

def test_next_position_right_not_start(): 
    assert next_position(1, 4, Dir.RIGHT) == 2

def test_accessing_position_out_of_puzzle():
    with pytest.raises(Exception, match="out of bounds"):
        next_position(3,4,Dir.RIGHT)

def test_next_position_easy_down():
    assert next_position(0,4,Dir.DOWN) == 4

def test_next_position_down_out_of_puzzle():
    with pytest.raises(Exception, match="out of bounds"):
        next_position(15,4,Dir.DOWN)

def test_next_position_up_out_of_puzzle():
    with pytest.raises(Exception, match="out of bounds"):
        next_position(0,4,Dir.UP)

def test_easy_up():
    assert next_position(4,4,Dir.UP) == 0

def test_working_diagonally():
    assert next_position(0,4,Dir.RIGHT_DOWN) == 5

def test_not_working_diagonally():
    with pytest.raises(Exception, match="out of bounds"):
        next_position(8,4,Dir.LEFT_UP)

def test_given_dummy_input():
    puzzle = read_input_from_file("./given_dummy_input.txt")
    assert count_whole_puzzle(puzzle) == 18

def test_given_dummy_input_22_pos():
    puzzle = read_input_from_file("./given_dummy_input.txt")
    assert count_at_coordinate(puzzle,22) == 0

def test_given_input_second_task():
    puzzle = read_input_from_file("./given_dummy_input.txt")
    assert count_MAS_whole_puzzle(puzzle) == 9