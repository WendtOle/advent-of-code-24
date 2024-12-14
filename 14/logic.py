def generate_picture(enries, dimensions):
    [width, height] = dimensions
    current_min = None
    for i in range(10000):
        picture = list(map(lambda entry: get_position(entry[0], entry[1],dimensions, i),enries))
        overlapping = len(picture) - len(set(picture))
        if current_min is None or overlapping < current_min:
            current_min = overlapping
            print(f"seconds {i} - {overlapping}")
            print_positions(picture, width, height)

def get_safety_factor(file_name, width, height):
    robot_entries = read_input(file_name)

    width_middle = width // 2
    height_middle = height // 2

    after_100_seconds = []
    left_up, left_down, right_up, right_down = [],[],[],[]

    for [position, velocity] in robot_entries:
        new_position = get_position(position,velocity, (width, height), 100)
        [x_new, y_new] = new_position
        if (x_new < width_middle and y_new < height_middle):
            left_up.append(new_position)
        if (x_new < width_middle and y_new > height_middle):
            left_down.append(new_position)
        if (x_new > width_middle and y_new < height_middle):
            right_up.append(new_position)
        if (x_new > width_middle and y_new > height_middle):
            right_down.append(new_position)
        
        after_100_seconds.append(new_position)

    return len(left_up) * len(left_down) * len(right_up) * len(right_down)

def print_positions(positions, width, height):
    for y in range(height):
        for x in range(width):
            found_entries = 0
            for entry in positions:
                if entry[0] == x and entry[1] == y:
                    found_entries += 1
            if found_entries == 0:
                print(".", end="")
            else:
                print(found_entries, end="")
        print("",end="\n")

def test_get_safety_factor():
    assert get_safety_factor("./example.txt", 11, 7) == 12

def get_position(position, velocity, dimensions, seconds):
    [x,y] = position
    [x_vel, y_vel] = velocity
    [width, height] = dimensions
    x_target = x + x_vel * seconds
    y_target = y + y_vel * seconds
    return (x_target % width, y_target % height)

def test_get_position():
    assert get_position((2,4), (2,-3), (11,7),1) == (4,1)

def read_input(file_name):
    lines = None
    with open(file_name, 'r') as file:
        lines = file.readlines()
    robot_entries = []
    for line in lines:
        [position_string, velocity_string] = line.split(" ")
        position = tuple(prepare(position_string.replace("p=", "").split(",")))
        velocity = tuple(prepare(velocity_string.replace("v=", "").split(",")))
        robot_entries.append([position, velocity])
    return robot_entries

def prepare(input):
    return list(map(lambda entry: int(entry.strip()), input))
    
def test_read_input():
    assert read_input("./simple-example.txt") == [[(0,4),(3,-3)],[(6,3),(-1,-3)]]

if __name__ == "__main__":
    print(get_safety_factor("./puzzle.txt", 101, 103))
    
    entries = read_input("./puzzle.txt")

    generate_picture(entries,(101,103))