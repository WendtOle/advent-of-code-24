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
    #print_map(input, width)
    #print(moves, move, robot_index)
    sorted_moves = sorted(moves, key=lambda x: x[1], reverse=(move == Direction.DOWN or move == Direction.RIGHT))
    #print(moves, sorted_moves)
    return do_actual_moves(input, sorted_moves)

def get_moves(input, index, height, width, direction: Direction, moves = []):
    #print(width)
    sign_to_move = input[index]
    box_to_move = sign_to_move == Sign.BOX_LEFT or sign_to_move == Sign.BOX_RIGHT
    vertical_box_move = box_to_move and (direction == Direction.DOWN or direction == Direction.UP)
    if vertical_box_move:
        return get_vertical_box_moves(input, index, height, width, direction, moves)
    return simple_get_moves(input, index, height, width, direction, moves)
    
def get_vertical_box_moves(input, index, height, width, direction: Direction, moves = []):
    [left, right] = (index, index + 1) if input[index] == Sign.BOX_LEFT else (index - 1, index)
    left_index_after_move = get_position_after_move(left, height, width, direction)
    right_index_after_move = get_position_after_move(right, height, width, direction)
    
    left_sign_to_move_onto = input[left_index_after_move]
    right_sign_to_move_onto = input[right_index_after_move]

    moves_against_wall = left_sign_to_move_onto == Sign.WALL or right_sign_to_move_onto == Sign.WALL
    if moves_against_wall:
        return []
    
    moves_on_empty = left_sign_to_move_onto == Sign.EMPTY and right_sign_to_move_onto == Sign.EMPTY
    if moves_on_empty:
        return [(left, left_index_after_move), (right, right_index_after_move)] + moves
    
    moves_against_box = left_sign_to_move_onto == Sign.BOX_LEFT or left_sign_to_move_onto == Sign.BOX_RIGHT or right_sign_to_move_onto == Sign.BOX_LEFT or right_sign_to_move_onto == Sign.BOX_RIGHT
    if moves_against_box:
        left_moves = get_moves(input, left_index_after_move, height, width, direction, [(left, left_index_after_move)] + moves)
        right_moves = get_moves(input, right_index_after_move, height, width, direction, [(right, right_index_after_move)] + moves)
        if len(left_moves) == 0 or len(right_moves) == 0:
            return []
        moves_to_return = set()
        moves_to_return.update(left_moves)
        moves_to_return.update(right_moves)
        return moves_to_return

    raise Exception("left is 'move against robot' - but this should not be possible")

def simple_get_moves(input, index, height, width, direction: Direction, moves = []):
    index_after_move = get_position_after_move(index, height, width, direction)
    sign_to_move_onto = input[index_after_move]
    moves_against_wall = sign_to_move_onto == Sign.WALL
    if moves_against_wall:
        return []
    moves_on_empty = sign_to_move_onto == Sign.EMPTY
    move = (index, index_after_move)
    if moves_on_empty:
        return [move] + moves
    moves_against_box = sign_to_move_onto == Sign.BOX or sign_to_move_onto == Sign.BOX_LEFT or sign_to_move_onto == Sign.BOX_RIGHT
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
        raise Exception("move on not empty space is not possible", end_sign, start, "->", end)
    sign_to_move = input[start]
    if sign_to_move == Sign.EMPTY:
        return input
    large_box = sign_to_move == Sign.BOX_RIGHT or sign_to_move == Sign.BOX_LEFT
    if sign_to_move == Sign.BOX or sign_to_move == Sign.ROBOT or large_box:
        return simple_move(input, start, end)
    raise Exception("only boxes or the robot should be moved")

def simple_move(input: str, start: int, end: int):
    sign_to_move = input[start]
    as_list = list(input)
    as_list[start] = Sign.EMPTY
    as_list[end] = sign_to_move
    return "".join(as_list)

def vertical_box_move(input: str, start: int, end: int):
    sign_to_move = input[start]
    modificator = 1 if sign_to_move == Sign.BOX_LEFT else -1
    as_list = list(input)
    as_list[start] = Sign.EMPTY
    as_list[start + modificator] = Sign.EMPTY
    as_list[end] = sign_to_move 
    as_list[end + modificator] = other_box_end(sign_to_move)
    return "".join(as_list)

def other_box_end(sign: Sign):
    if sign == Sign.BOX_LEFT:
        return Sign.BOX_RIGHT
    return Sign.BOX_LEFT

def print_map(input, width, index=0):
    if len(input) == 0:
        return
    print(index, input[:width])
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
