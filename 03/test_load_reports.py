from load_memory import load_memory

def test_load_lists():
    assert load_memory("./dummy-input.txt") == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def test_load_memory_through_multiple_lines():
    assert load_memory("./dummy-2-input.txt") == "123"