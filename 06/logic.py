import math
from enum import Enum
from load_input import read_input_from_file


def walk_guard(puzzle):
    width = get_width(puzzle)
    cur_pos = get_guard_position(puzzle)
    cur_dir = Dir.UP
    positions = [cur_pos]
    while cur_pos in positions:
        try: 
            next_pos = next_position(cur_pos, width, cur_dir)
        except Exception:
            return positions
        next_object = puzzle[next_pos]
        if next_object == "#":
            next_dir_index = order.index(cur_dir) + 1
            if next_dir_index >= 4:
                next_dir_index = 0
            next_dir = order[next_dir_index]
            cur_dir = next_dir
            try: 
                next_pos = next_position(cur_pos, width, cur_dir)
            except Exception:
                return positions
        
        cur_pos = next_pos
        positions.append(cur_pos)

# next step would be to track exactly where it goes in the minimal example
# maybe i can observe some thing what goes wrong
# and the output of 6 is only by accident 

def mislead_the_guard(puzzle):
    width = get_width(puzzle)
    cur_pos = get_guard_position(puzzle)
    cur_dir = Dir.UP
    obstacles_bounced = []
    here_obstacle_would_lead_to_loop = []
    while True:
        try: 
            next_pos = next_position(cur_pos, width, cur_dir)
        except Exception:
            break
        next_object = puzzle[next_pos]
        next_dir_index = order.index(cur_dir) + 1
        if next_dir_index >= 4:
            next_dir_index = 0
        next_dir_if_bounces = order[next_dir_index]
        if next_object == "#":
            cur_dir = next_dir_if_bounces
            obstacles_bounced.append(next_pos)
        else:
            if would_bounce_on_already_meet_object(puzzle, obstacles_bounced,next_dir_if_bounces, cur_pos):
                here_obstacle_would_lead_to_loop.append(next_pos)

        try: 
            next_pos = next_position(cur_pos, width, cur_dir)
        except Exception:
            break
        cur_pos = next_pos
    print(obstacles_bounced, here_obstacle_would_lead_to_loop)
    for pos in here_obstacle_would_lead_to_loop:
        print(int(pos % width), int(pos // width))
    print(len(here_obstacle_would_lead_to_loop))
    
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
    
    target_column = step[dir][0] + column
    target_row = step[dir][1] + row

    if target_column < 0 or target_column >= width or target_row < 0 or target_row >= width: 
        raise Exception("out of bounds")
        
    return int(target_column + target_row * width)


if __name__ == "__main__":
    puzzle = read_input_from_file("./given-input.txt")
    
    #path = walk_guard(puzzle)
    #distinct = list(set(path))
    #print(len(distinct))

    mislead_the_guard(puzzle)