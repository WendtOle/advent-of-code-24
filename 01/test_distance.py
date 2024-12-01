from distance import distance
from load_lists import load_lists


def test_distance_between_two_numbers(): 
    assert distance([1],[2]) == 1

def test_distance_between_list_of_two_entries():
    assert distance([1,1],[2,2]) == 2

def test_distance_when_left_is_larger_than_right():
    assert distance([2,2],[1,1]) == 2

def test_distance_when_lists_are_not_sorted():
    assert distance([1,1,3],[2,1,1]) == 1

def test_distance_from_dummy_input(): 
    [left, right] = load_lists("./01/dummy-puzzle-input.txt")
    assert distance(left, right) == 11
