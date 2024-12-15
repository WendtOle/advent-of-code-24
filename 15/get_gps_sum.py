import enum


class Sign(str, enum.Enum):
    WALL = "#",
    BOX = "O",
    ROBOT = "@",
    EMPTY = "."

def get_gps_sum(input, width, index=0):
    if index >= len(input):
        return 0
    current_gps = get_current_gps(input, width, index)
    return get_gps_sum(input, width, index + 1) + current_gps

def get_current_gps(input, width, index):
    if input[index] == Sign.BOX:
        return get_gps(index, width)
    return 0

def get_gps(index, width):
    column, row = index % width, index // width
    return column + 100 * row

