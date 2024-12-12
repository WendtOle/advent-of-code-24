def transform_stone(stone):
    [engraving, multiplier] = stone
    if engraving == 0:
        return [(1,multiplier)]
    engraving_as_string = str(engraving)
    if len(engraving_as_string) % 2 == 0:
        middle_index = int(len(engraving_as_string) / 2)
        return [(int(engraving_as_string[:middle_index]),multiplier), (int(engraving_as_string[middle_index:]),multiplier)]
    return [(engraving * 2024,multiplier)]

def blink(stones, stone_memory):
    stones_after_blink = []
    for stone in stones:
        stones_to_add = None
        if stone in stone_memory:
            stones_to_add = stone_memory[stone]
        else:
            stones_to_add = transform_stone(stone)
            stone_memory[stone] = stones_to_add
        left = stones_to_add[0]
        if left in stones_after_blink:
            index = stones_after_blink.index(left)
            [engraving, multiplier] = stones_after_blink[index] 
            stones_after_blink[index] = (engraving, multiplier + left[1])
            if len(stones_to_add) == 2:
                stones_after_blink += [stones_to_add[1]]
        else:
            stones_after_blink += stones_to_add
    return [stones_after_blink, stone_memory]

def blink_often(stones,times):
    transformed_stones = list(map(lambda stone: (stone, 1), stones))
    stone_memory = {}
    for i in range(times):
        if i % 5 == 0:
            print("blink", i)
        [updated_transformed_stones, updated_stone_memory] = blink(transformed_stones, stone_memory)
        transformed_stones = updated_transformed_stones
        stone_memory = updated_stone_memory
    counter = 0
    for entry in transformed_stones:
        counter += entry[1]
    return counter

import time

if __name__ == "__main__":
    input = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]

    start_time = time.time() 
    print(blink_often(input,75))
    end_time = time.time()
    print("time elapsed", end_time - start_time)

"""
Idea is to save an engraving in a hashmap
and to how many stones this stone transforms
this can be done again and again to find the number
"""