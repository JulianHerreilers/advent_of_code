import numpy as np
import re
import random
from tqdm import tqdm

guard_position = ()
guard_x, guard_y = 0, 0
v_y, v_x = 0, 0

with open('AOC_2024/day7.txt', 'r') as f:
    data =  f.readlines()

answers = []
inputs = []


part1_ans = 0

for line in data:
    nums = list(map(int, line.strip().replace(":","").split()))
    answers.append(nums[0])
    inputs.append(nums[1:])

def check_eq(ans, inputs):
    possible_combinations = []
    for num in inputs:
        if len(possible_combinations):
            updated_combinations = []
            for combination in possible_combinations:
                updated_combinations.append(combination+num)
                updated_combinations.append(combination*num)
            possible_combinations = updated_combinations
        
        else: 
            possible_combinations.append(num)
        
    return ans in possible_combinations    

def check_eq_part2(ans, inputs):
    possible_combinations = []
    for num in inputs:
        if len(possible_combinations):
            updated_combinations = []
            for combination in possible_combinations:
                updated_combinations.append(combination+num)
                updated_combinations.append(combination*num)
                updated_combinations.append(int(str(combination)+str(num)))
            possible_combinations = updated_combinations
        
        else: 
            possible_combinations.append(num)
        
    return ans in possible_combinations    
        
not_part1_valid = []
for i in range(len(answers)):
    if check_eq(answers[i], inputs[i]): 
        part1_ans += answers[i]
    else:
        not_part1_valid.append(i)

print(f"Part 1:", part1_ans)

for i in not_part1_valid:
    if check_eq_part2(answers[i], inputs[i]): 
        part1_ans += answers[i]

print(f"Part 2:", part1_ans)
