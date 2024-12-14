def get_antenna_locations(file_name):
    lines = None
    with open(file_name, 'r') as file:
        lines = file.readlines()
    dimensions = (len(lines[0].strip()), len(lines))
    print(dimensions)
    antennas = {}
    for y,line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != ".":
                if not(char in antennas):
                    antennas[char] = []
                antennas[char].append((x,y))
    return [antennas, dimensions]

def test_get_antenna_locations():
    assert get_antenna_locations("./example.txt") == [{'0': [(8, 1), (5, 2), (7, 3), (4, 4)], 'A': [(6, 5), (8, 8), (9, 9)]}, (13, 12)]

from itertools import combinations

def generate_anti_node_positions(antennas, dimensions):
    antenna_pairs = list(combinations(antennas, 2))
    antinodes = []
    for [left, right] in antenna_pairs:
        [x_left, y_left] = left
        [x_right, y_right] = right
        x_step = x_right - x_left
        y_step = y_right - y_left

        antinodes += [left, right]
        antinodes += generate_antinodes(left, (x_step * -1, y_step * -1), dimensions)
        antinodes += generate_antinodes(right, (x_step, y_step), dimensions)
    return antinodes

def generate_antinodes(origin, step, dimensions):
    [x_step, y_step] = step
    antinodes = []
    current = origin
    while True:
        [x,y] = current
        new_node = (x + x_step,y + y_step)
        if not in_raster(new_node, dimensions):
            break;
        antinodes.append(new_node)
        current = new_node
    return antinodes

def in_raster(position, dimension):
    [x,y] = position
    [width, height] = dimension
    if x < 0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return True

def generate_all_antinodes(file_name):
    [antennas, dimensions] = get_antenna_locations(file_name)
    antinodes = []
    for key in antennas.keys():
        antinodes += generate_anti_node_positions(antennas[key], dimensions)
    unique = list(set(antinodes))
    print_positions(antennas, unique, dimensions)
    print(antennas)
    print(unique)
    return len(unique)

def print_positions(antenna_positions, antinode_positions, dimensions):
    [width, height] = dimensions
    for y in range(height):
        for x in range(width):
            print(get_symbol_for_pos((x,y), antenna_positions, antinode_positions),end="")
        print("",end="\n")

def get_symbol_for_pos(pos, antenna_positions, antinode_positions):
    [x,y] = pos
    for key in antenna_positions.keys():
        for entry in antenna_positions[key]:
            if entry[0] == x and entry[1] == y:
                return key
    for entry in antinode_positions:
        if entry[0] == x and entry[1] == y:
            return "#"
    return "."

def test_generate_anti_node_positions():
    assert generate_all_antinodes("./example.txt") == 34

def test_generate_anti_node_positions_2():
    assert generate_all_antinodes("./another-example.txt") == 9

if __name__ == "__main__":
    print(generate_all_antinodes("./given.txt"))