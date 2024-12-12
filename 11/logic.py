def transform_stone(engraving):
    if engraving == 0:
        return [1]
    engraving_as_string = str(engraving)
    if len(engraving_as_string) % 2 == 0:
        middle_index = int(len(engraving_as_string) / 2)
        return [int(engraving_as_string[:middle_index]), int(engraving_as_string[middle_index:])]
    return [engraving * 2024]

def blink(stones):
    stones_after_blink = []
    for stone in stones:
        stones_after_blink += transform_stone(stone)
    return stones_after_blink

def blink_often(stones,times):
    previous = stones
    transformed_stones = stones
    for i in range(times):
        transformed_stones = blink(transformed_stones)
        print("blink", i, len(transformed_stones) - len(previous))
        previous = transformed_stones
    return len(transformed_stones)

if __name__ == "__main__":
    input = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]
    print(blink_often(input,40))

"""
Idea is to save an engraving in a hashmap
and to how many stones this stone transforms
this can be done again and again to find the number
"""