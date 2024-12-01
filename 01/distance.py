from load_lists import load_lists

def distance (left_unsorted, right_unsorted):
    left = sorted(left_unsorted)
    right = sorted(right_unsorted)
    total_distance = 0
    for (index, left_value) in enumerate(left):
        right_value = right[index]
        total_distance += abs(right_value - left_value)
    return total_distance

if __name__== "__main__":
    [left, right] = load_lists("./01/puzzle-input.txt")
    print(distance(left, right))