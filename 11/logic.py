def transform_stone(engraving):
    if engraving == 0:
        return [1]
    engraving_as_string = str(engraving)
    if len(engraving_as_string) % 2 == 0:
        middle_index = int(len(engraving_as_string) / 2)
        return [int(engraving_as_string[:middle_index]), int(engraving_as_string[middle_index:])]
    return [engraving * 2024]

def blink(stones, stone_memory):
    stones_after_blink = []
    for stone in stones:
        if stone in stone_memory:
            stones_after_blink += stone_memory[stone]
            continue
        transformed_stones = transform_stone(stone)
        stone_memory[stone] = transformed_stones
        stones_after_blink += transformed_stones
    return [stones_after_blink, stone_memory]

def blink_often(stones,times):
    transformed_stones = stones
    stone_memory = {}
    for i in range(times):
        if i % 5 == 0:
            print("blink", i)
        [updated_transformed_stones, updated_stone_memory] = blink(transformed_stones, stone_memory)
        transformed_stones = updated_transformed_stones
        stone_memory = updated_stone_memory
    return len(transformed_stones)

import time

if __name__ == "__main__":
    input = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]

    start_time = time.time() 
    print(blink_often(input,40))
    end_time = time.time()
    print("time elapsed", end_time - start_time)

"""
Idea is to save an engraving in a hashmap
and to how many stones this stone transforms
this can be done again and again to find the number
"""