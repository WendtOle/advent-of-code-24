from load_lists import load_lists

def similarity(left, right):
    right_lookup = {}
    for right_value in right:
        if (right_value in right_lookup):
            right_lookup[right_value] += 1
        else:
            right_lookup[right_value] = 1
    similarity = 0
    for left_value in left:
        if (left_value in right_lookup):
            similarity += left_value * right_lookup[left_value]
    return similarity

if __name__ == "__main__":
    [left, right] = load_lists("./01/puzzle-input.txt")
    print(similarity(left, right))