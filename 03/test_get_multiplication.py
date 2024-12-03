from get_multiplication import get_multiplication
from get_toggeable_multiplication import get_toggleable_multiplication

def test_get_dummy_multiplication_result():
    assert get_multiplication("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

def test_get_toggleable_multiplication():
    assert get_toggleable_multiplication("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48

def test_get_toggleable_multiplication_with_dont_dont():
    assert get_toggleable_multiplication("don't()_mul(5,5)don't()") == 0

def test_get_toggleable_multiplication_with_multiple_dont_dont():
    assert get_toggleable_multiplication("don't()_mul(5,5)don't()mul(5,5)don't()") == 0