import math
from enum import Enum
from read_input import read_input_from_file

target_word = "XMAS"

def count_at_coordinate(puzzle, position):
    count = 0
    for dir in step.keys():
        matched = matches(puzzle, position, dir)
        if matched:
            #print(position, dir)
            count += 1

    return count

def count_whole_puzzle(puzzle):
    count = 0
    for i, char in enumerate(puzzle):
        if char == target_word[0]:
            count += count_at_coordinate(puzzle, i)
    return count

def matches(puzzle, position, dir, depth = 0):
    if puzzle[position] != target_word[depth]:
        return False

    #print(position, dir)
    if depth == len(target_word) - 1:
        return True
    
    width = get_width(puzzle)

    try: 
        next_pos = next_position(position, width, dir)
        return matches(puzzle, next_pos, dir, depth + 1)
    except Exception as e:
        return False
    

def get_width(puzzle):
    width = math.sqrt(len(puzzle))
    if width % 2 != 0:
        raise Exception(f"invalid length {len(puzzle)}")
    return width

class Dir(Enum):
    LEFT = "left",
    RIGHT = "right",
    UP = "up"
    DOWN = "down",
    LEFT_DOWN = "left_down"
    LEFT_UP = "left_up",
    RIGHT_DOWN = "right_down",
    RIGHT_UP = "right_up"

step = {
    Dir.RIGHT: (1,0),
    Dir.LEFT: (-1, 0),
    Dir.DOWN: (0,1),
    Dir.UP: (0,-1),
    Dir.RIGHT_DOWN: (1,1),
    Dir.RIGHT_UP: (1,-1),
    Dir.LEFT_DOWN:(-1,1),
    Dir.LEFT_UP: (-1,-1)
}


def next_position(cur, width, dir: Dir):
    
    column = cur % width
    row = int(cur / width)
    
    target_column = step[dir][0] + column
    target_row = step[dir][1] + row

    if target_column < 0 or target_column >= width or target_row < 0 or target_row >= width: 
        raise Exception("out of bounds")
        
    return int(target_column + target_row * width)


if __name__ == "__main__":
    puzzle = read_input_from_file("./puzzle_input.txt")
    print(count_whole_puzzle(puzzle))