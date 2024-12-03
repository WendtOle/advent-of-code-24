import re
from load_memory import load_memory
from get_multiplication import get_multiplication

def get_toggleable_multiplication(memory):
    enabled_chars = ""
    current_buffer = ""
    is_enabled = True
    for char in memory:
        #print(char, enabled_chars, current_buffer, is_enabled)
        if is_enabled and "don't()" in current_buffer:
            enabled_chars += current_buffer
            current_buffer = ""
            is_enabled = False
        if not is_enabled and "do()" in current_buffer:
            current_buffer = ""
            is_enabled = True
        current_buffer += char
    if is_enabled:
        enabled_chars += current_buffer
    #print("memory", memory)
    #print("enabled_chars", enabled_chars)
    return get_multiplication(enabled_chars)


if __name__ == "__main__":
    memory = load_memory("./puzzle-input.txt")
    print(get_toggleable_multiplication(memory))