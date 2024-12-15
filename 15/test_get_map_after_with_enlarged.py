from main import execute_multiple_moves, print_map

def preprocess(input: str):
    return "".join(list(map(lambda line: line.strip(), input.split("\n"))))

initial = preprocess("""
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
""")

end = preprocess("""
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
""")

def test_end():
    actual = execute_multiple_moves(initial, "<vv<<^^<<^^", 14)
    assert actual == end

def test_own():
    input = preprocess("""
    ########
    #....#.#
    #..[][]#
    #...@..#
    #......#
    ########                
    """)
    acutal_out =  execute_multiple_moves(input, "^", 8)
    expected_out = preprocess("""
    ########
    #..[]#.#
    #...@[]#
    #......#
    #......#
    ########                
    """)
    assert acutal_out == expected_out