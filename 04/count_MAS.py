from read_input import read_input_from_file
from count_at_coordinate import Dir, next_position, get_width

combinations = [
    "MSSM",
    "SMMS",
    "SSMM",
    "MMSS"
]

def found_at_coordinate(puzzle, position):
    if puzzle[position] != "A":
        return False
    
    dirs_to_check = [
        Dir.LEFT_UP,
        Dir.RIGHT_UP,
        Dir.RIGHT_DOWN,
        Dir.LEFT_DOWN
    ]
    string = ""
    width = get_width(puzzle)
    for dir in dirs_to_check:
        try: 
            string += puzzle[next_position(position, width, dir)]
        except Exception:
            return False
    
    return string in combinations

def count_whole_puzzle(puzzle):
    count = 0
    for i, _ in enumerate(puzzle):
        if found_at_coordinate(puzzle,i):
            count += 1
    return count


if __name__ == "__main__":
    puzzle = read_input_from_file("./puzzle_input.txt")
    print(count_whole_puzzle(puzzle))