from enum import Enum
from get_gps_sum import Sign

class Direction(str, Enum):
    UP = "^",
    LEFT = "<",
    DOWN = "v",
    RIGHT = ">",

def get_map_after_move(input: str, width: int, move: Direction):
    robot_index = get_robot_index(input)
    height = len(input) // width
    moves = get_moves(input, robot_index, height, width, move)
    return do_actual_moves(input, moves)

def get_moves(input, index, height, width, direction: Direction, moves = []):
    index_after_move = get_position_after_move(index, height, width, direction)
    moves_against_wall = input[index_after_move] == Sign.WALL
    if moves_against_wall:
        return []
    moves_on_empty = input[index_after_move] == Sign.EMPTY
    move = (index, index_after_move)
    if moves_on_empty:
        return [move] + moves
    moves_against_box = input[index_after_move] == Sign.BOX
    if moves_against_box:
        return get_moves(input, index_after_move, height, width, direction, [move] + moves)
    raise Exception("left is 'move against robot' - but this should not be possible")

def do_actual_moves(input, moves):
    if len(moves) == 0:
        return input
    [start, end] = moves[0]
    return do_actual_moves(move(input, start, end), moves[1:])

def move(input: str, start: int, end: int):
    end_sign = input[end]
    if end_sign != Sign.EMPTY:
        raise Exception("move on not empty space is not possible")
    sign_to_move = input[start]
    if sign_to_move != Sign.BOX and sign_to_move != Sign.ROBOT:
        raise Exception("only boxes or the robot should be moved")
    as_list = list(input)
    as_list[start] = Sign.EMPTY
    as_list[end] = sign_to_move
    return "".join(as_list)

def print_map(input, width, index=0):
    if len(input) == 0:
        return
    print(input[:width])
    print_map(input[width:], width, index + 1)
    return

def get_position_after_move(index: int, height: int, width: int, move: Direction):
    if Direction.DOWN == move:
        return index + width if index + width < height * width else index
    if Direction.UP == move:
        return index - width if index - width >= 0 else index
    current_line_index = index // width
    lin_min = current_line_index * width
    line_max = (current_line_index + 1) * width
    if Direction.LEFT == move:
        return index - 1 if index - 1 >= lin_min else index
    return index + 1 if index + 1 < line_max else index

def get_robot_index(input: str, index=0):
    as_list = list(input)
    if Sign.ROBOT in as_list:
        return as_list.index(Sign.ROBOT)
    raise Exception("no robot position found in input")
