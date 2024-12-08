import numpy as np
import re

part1_correct = 0
lines = []

with open('AOC_2024/day4.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip())


pattern = ["XMAS","SAMX"]

horizontal_correct = 0
vertical_correct = 0
diagonal_correct = 0


# Check horizontal correct
for line in lines:
    for i in range(len(line)-3):
        if line[i:i+4] in pattern:
            horizontal_correct+=1


# Check vertical correct
for col in range(len(lines[0])):
    for i in range(len(lines)-3):
        match = "".join(lines[j][col] for j in range(i, i+4))
        if match in pattern:
            vertical_correct+=1

# Check diagonal correct
idx_x = 0
idx_y = 0  
lr_n, rl_n = 0, 0 
for idx_y in range(len(lines)-3):
    lr_match, rl_match  = "", ""
    for idx_x in range(len(lines[idx_y])):
        if idx_x < len(lines[0])-3 and idx_y < len(lines)-3:
            lr_match = "".join(lines[y][x] for y,x in zip(range(idx_y, idx_y+4), range(idx_x, idx_x+4)))
            if lr_match in pattern: 
                lr_n+=1
        
        if idx_x>=3:
            rl_match = "".join(lines[y][idx_x-x] for y,x in zip(range(idx_y, idx_y+4), range(0, 4)))
            if rl_match in pattern: 
                rl_n+=1

print("Part 1:",horizontal_correct, vertical_correct, lr_n, rl_n, "Total:",sum([horizontal_correct, vertical_correct, (lr_n+ rl_n)]))

part2_correct = 0

pattern = ["MAS","SAM"]

size_x =len(lines[0])
size_y = len(lines)
for idx_y in range(1,size_y-1):
    lr_match, rl_match  = "", ""
    for idx_x in range(1,size_x-1):
        if 0 < idx_x < size_x-1 and 0< idx_y < size_y-1:
            lr_match = "".join(lines[y][x] for y,x in zip(range(idx_y-1, idx_y+2), range(idx_x-1, idx_x+2)))
            if lr_match in pattern: 
                rl_match = "".join(lines[y][idx_x-x] for y,x in zip(range(idx_y-1, idx_y+2), range(-1, 2)))
                if rl_match in pattern: 
                    part2_correct+=1

print("Part 2:",part2_correct)
