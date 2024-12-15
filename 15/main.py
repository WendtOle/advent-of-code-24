from get_map_after_move import get_map_after_move, print_map
from get_gps_sum import get_gps_sum

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(22000)
print(sys.getrecursionlimit())

def execute_multiple_moves(input, moves, width):
    if len(moves) == 0:
        return input
    output = get_map_after_move(input, width, moves[0])
    print(len(moves))
    left_moves = moves[1:]
    return execute_multiple_moves(output, left_moves, width)

def read_input(file_name):
    lines = None
    with open(file_name, 'r') as file:
        lines = file.readlines()
    empty_line_index = lines.index("\n")
    input = "".join(list(map(lambda line: line.strip(), lines[:empty_line_index])))
    moves = "".join(list(map(lambda line: line.strip(), lines[empty_line_index:])))
    width = len(lines[0].strip())
    return [input, width, moves]

if __name__ == "__main__":
    [input, width, moves] = read_input("./puzzle.txt")
    end = execute_multiple_moves(input, moves, width)
    print(get_gps_sum(end, width))
    
