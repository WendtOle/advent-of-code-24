from get_map_after_move import get_map_after_move, Direction, get_robot_index, get_position_after_move, print_map

def preprocess(input: str):
    return "".join(list(map(lambda line: line.strip(), input.split("\n"))))

initial = preprocess("""
    ########
    #..O.O.#
    ##@.O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########
    """)

one_move_up = preprocess("""
    ########
    #.@O.O.#
    ##..O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########
    """) 

one_move_up_move_right = preprocess("""
    ########
    #..@OO.#
    ##..O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########
    """) 

def test_get_robot_index():
    assert get_robot_index(initial) == 18

def test_get_position_after_move():
    assert get_position_after_move(11,10,10,Direction.UP) == 1

def test_move_against_wall():
    assert get_map_after_move(initial, 8, Direction.LEFT) == initial

def test_move_against_single_object():   
    actual = get_map_after_move(one_move_up, 8, Direction.RIGHT)
    print_map(one_move_up,8)
    print_map(actual,8)
    assert actual == one_move_up_move_right

