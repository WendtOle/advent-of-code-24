import math
from enum import Enum
from load_input import read_input_from_file


def walk_guard(puzzle, obsticle):
    width = get_width(puzzle)
    cur_pos = get_guard_position(puzzle)
    cur_dir = Dir.UP
    steps = 1
    while True:
        if steps > 25000:
            return True
        try: 
            next_pos = next_position(cur_pos, width, cur_dir)
        except Exception:
            return False
        next_object = puzzle[next_pos]
        if next_object == "#" or next_pos == obsticle:
            next_dir_index = order.index(cur_dir) + 1
            if next_dir_index >= 4:
                next_dir_index = 0
            next_dir = order[next_dir_index]
            cur_dir = next_dir
            try: 
                next_pos = next_position(cur_pos, width, cur_dir)
            except Exception:
                return False
        
        cur_pos = next_pos
        steps += 1

# next step would be to track exactly where it goes in the minimal example
# maybe i can observe some thing what goes wrong
# and the output of 6 is only by accident 

def mislead_the_guard(puzzle):
    width = int(get_width(puzzle))

    counter = 0
    for pos in range(width ** 2):
        if walk_guard(puzzle, pos):
            counter += 1
            print(pos, counter)

    return counter


    """
    for path in output:
        for pos in path:
            print(int(pos % width), int(pos // width))
        print()"""
    return len(output)

def recursive(puzzle, current_position, current_direction, obstacles_bounced = [], possible_obsticle_place_was_set = None):
    width = get_width(puzzle)
    next_pos = None
    try: 
        next_pos = next_position(current_position, width, current_direction)
    except Exception:
        return []
    paths = []
    next_object = puzzle[next_pos]
    if next_pos in obstacles_bounced and possible_obsticle_place_was_set != None :
        return [obstacles_bounced]
    if next_object == "#":
        path_when_bounced = recursive(puzzle, current_position, next_direction(current_direction), obstacles_bounced + [next_pos], possible_obsticle_place_was_set)
        for path in path_when_bounced:
            paths.append(path)
    else:
        if possible_obsticle_place_was_set == None:
            path_if_woud_bounced = recursive(puzzle, current_position, next_direction(current_direction), obstacles_bounced + [next_pos], next_pos)
            for path in path_if_woud_bounced:
                paths.append(path)
        path_if_would_not_bounced = recursive(puzzle, next_pos, current_direction, obstacles_bounced, possible_obsticle_place_was_set)
        for path in path_if_would_not_bounced:
            paths.append(path)
    return paths

def next_direction(cur_dir):
    next_dir_index = order.index(cur_dir) + 1
    if next_dir_index >= 4:
        next_dir_index = 0
    next_dir_if_bounces = order[next_dir_index]   
    return next_dir_if_bounces 

def would_bounce_on_already_meet_object(puzzle, obstacles_bounced, direction,cur_pos):
    width = get_width(puzzle)
    if len(obstacles_bounced) == 0:
        return False
    next_pos = cur_pos
    while True:
        if next_pos in obstacles_bounced:
            return True
        try: 
            next_pos = next_position(next_pos, width, direction)
        except Exception:
            return False
    


def get_guard_position(puzzle):
    return puzzle.index("^")

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

order = [
    Dir.DOWN,
    Dir.LEFT,
    Dir.UP,
    Dir.RIGHT
]

step = {
    Dir.RIGHT: (1,0),
    Dir.LEFT: (-1, 0),
    Dir.DOWN: (0,1),
    Dir.UP: (0,-1),
}


def next_position(cur, width, dir: Dir):
    column = cur % width
    row = int(cur / width)
    #print(column, row)
    target_column = step[dir][0] + column
    target_row = step[dir][1] + row

    #print(target_column, target_row)

    if target_column < 0 or target_column >= width or target_row < 0 or target_row >= width: 
        raise Exception("out of bounds")
        
    return int(target_column + target_row * width)


if __name__ == "__main__":
    puzzle = read_input_from_file("./puzzle-input.txt")
    
    #path = walk_guard(puzzle)
    #distinct = list(set(path))
    #print(len(distinct))

    output = mislead_the_guard(puzzle)
    print(output)