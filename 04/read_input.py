def read_input_from_file(file_name):
    lines = None
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return "".join(map(lambda line: line.strip(), lines))

