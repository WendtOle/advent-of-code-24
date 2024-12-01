def load_lists(file_name): 
    with open(file_name, 'r') as file:
        lines = file.readlines()

    left, right = [], []
    for line in lines:
        splitted = line.strip().split()
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))
    
    return [left, right]