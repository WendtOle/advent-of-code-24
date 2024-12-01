from load_lists import load_lists

def test_load_lists():
    assert load_lists("./01/dummy-puzzle-input.txt") == [[3,4,2,1,3,3],[4,3,5,3,9,3]]