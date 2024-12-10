from logic import mislead_the_guard, Dir
from load_input import read_input_from_file

def test_bounces_on_not_previously_seen_obsticle():
    input = """
    ......
    ...#..
    .....#
    ......
    ..#^..
    ......
    """
    output = mislead_the_guard("".join(map(lambda line: line.strip(), input)))
    print("output", output)
    assert output == 1

def test_given_example():
    puzzle = read_input_from_file("./given-input.txt")
    output = mislead_the_guard(puzzle)
    assert output == 6