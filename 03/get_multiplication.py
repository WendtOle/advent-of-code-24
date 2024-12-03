import re
from load_memory import load_memory

def get_multiplication(memory): 
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    result = 0
    for [left,right] in matches:
        sub_result = int(left) * int(right)
        result += sub_result
    return result


if __name__ == "__main__":
    memory = load_memory("./puzzle-input.txt")
    print(get_multiplication(memory))