from functools import cache

with open('AOC_2024/data/day11.txt', 'r') as f:
    stones= f.readline().strip().split()

print(stones)
def part_1(stones, max_blinks):
    for i in range(1,max_blinks+1):
        end_turn_stones = []
        for stone in stones:
            if stone == '0':
                end_turn_stones.append('1')
            elif len(stone)%2==0:
                stone_1 = stone[:len(stone)//2]
                stone_2 = stone[len(stone)//2:]
                end_turn_stones.append(str(int(stone_1)))
                end_turn_stones.append(str(int(stone_2)))
            else:
                end_turn_stones.append(str(int(stone)*2024))
        stones = end_turn_stones
        # print(f"turn {i}: {len(stones)}")
    return len(stones)

# Credits to HyperNeutrino for showing me about this cache library. 
# I tried to split each stone up and pass it completely but this did not work and still ran into ram issues.
@cache
def part_2(stone, steps):
    if steps== 0: return 1
    if stone == '0': return part_2('1', steps-1)

    elif len(stone)%2==0:
        stone_1 = stone[:len(stone)//2]
        stone_2 = stone[len(stone)//2:]
        return part_2(str(int(stone_1)),  steps -1) + part_2(str(int(stone_2)),  steps - 1)
    else:
        return part_2(str(int(stone)*2024), steps-1)

        
print(f"Part 1:", part_1(stones, 25)) 
print(f"Part 2:", sum([part_2(x, 75) for x in stones])) 