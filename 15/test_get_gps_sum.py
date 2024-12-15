from get_gps_sum import get_gps_sum

def test_get_gps_sum():
    input = "########...O..#......"
    assert get_gps_sum(input, 7) == 104

def test_get_gps_sum_with_enlarged():
    input = "############...[]...##........"
    assert get_gps_sum(input, 10) == 105