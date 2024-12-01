import pytest
from load_lists import load_lists
from similarity import similarity

def test_similarity_between_two_numbers():
    assert similarity([1],[1]) == 1

def test_similarity_when_first_number_appears_twice_right():
    assert similarity([1,2],[1,1]) == 2

#@pytest.mark.skip(reason="not yet ready")
def test_similarity_from_dummy_input(): 
    [left, right] = load_lists("./01/dummy-puzzle-input.txt")
    assert similarity(left, right) == 31