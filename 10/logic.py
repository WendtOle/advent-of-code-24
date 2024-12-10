def get_sum(input: str):
    splitted = input.split("\n")
    joined = "".join(map(lambda line: line.strip(), splitted))
    as_int = list(map(lambda char: int(char), joined))
    width = len(input.strip().split("\n")[0].strip())
    count = 0
    for index, char in enumerate(as_int):
        if char == 0:
            ends = set(recursive(0, index, as_int, width))
            count += len(ends) 
    return count

def recursive(current_level, current_position, puzzle, width):
    next_positions = get_surrounded_next_level(current_level, current_position, puzzle, width)
    if current_level == 8:
        return next_positions
    trail_ends = []
    for position in next_positions:
        trail_ends = trail_ends + recursive(current_level + 1, position, puzzle, width)
    return trail_ends

def get_surrounded_next_level(current_level, current_position, puzzle, width):
    positions = get_surrounded_positions(current_position, width)
    positions_with_next_level_and_none = list(map(lambda position: method(position, puzzle, current_level), positions))
    return filter_out_none(positions_with_next_level_and_none)

def method(position, puzzle, current_level):
    return position if puzzle[position] == current_level + 1 else None

def get_surrounded_positions(current_position, width):
    min_in_row = (current_position // width) * width
    max_in_row = ((current_position // width) + 1) * width
    max = width ** 2

    left = current_position - 1
    right = current_position + 1
    up = current_position - width
    down = current_position + width

    positions_with_none = [
        left if left >= min_in_row else None,
        right if right < max_in_row else None,
        up if up >= 0 else None,
        down if down < max else None
    ]
    return filter_out_none(positions_with_none)

    
def filter_out_none(list):
    return [x for x in list if x is not None]

if __name__ == "__main__":
    lines = None
    with open("./puzzle.txt", 'r') as file:
        lines = file.readlines()
    puzzle = "".join(lines)
    print(puzzle)
    print(get_sum(puzzle))
    