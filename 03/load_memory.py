def load_memory(file_name): 
    result = ""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            result += line.strip()
    return result 