from get_gps_sum import get_gps_sum

def test_get_gps_sum():
    input = "########...O..#......"
    assert get_gps_sum(input, 7) == 104