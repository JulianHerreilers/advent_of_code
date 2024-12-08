import numpy as np
import re
import random
from tqdm import tqdm

def create_antinodes_p1(antenna_y, antenna_x, input_map, antinode_map):
    for j in range(len(input_map)):
        for i in range(len(input_map[0])):
            if j != antenna_y and i != antenna_x:
                if input_map[antenna_y][antenna_x] == input_map[j][i]:
                    dy = antenna_y - j
                    dx = antenna_x - i

                    if 0<=antenna_y+dy<len(input_map) and 0<=antenna_x+dx<len(input_map[0]) :
                        antinode_map[antenna_y+dy, antenna_x+dx] = 1
                    if 0<=antenna_y-2*dy<len(input_map) and 0<=antenna_x-2*dx<len(input_map[0]) :
                        antinode_map[antenna_y-2*dy, antenna_x-2*dx] = 1     
    return antinode_map

def create_antinodes_p2(antenna_y, antenna_x, input_map, antinode_map):
    for j in range(len(input_map)):
        for i in range(len(input_map[0])):
            if j != antenna_y and i != antenna_x:
                if input_map[antenna_y][antenna_x] == input_map[j][i]:
                    dy = antenna_y - j
                    dx = antenna_x - i
                    k = 1
                    while 0<=antenna_y+k*dy<len(input_map) and 0<=antenna_x+k*dx<len(input_map[0]):
                        antinode_map[antenna_y+k*dy, antenna_x+k*dx] = 1
                        k += 1
                    
                    k = 1
                    while 0<=antenna_y-k*dy<len(input_map) and 0<=antenna_x-k*dx<len(input_map[0]) :
                        antinode_map[antenna_y-k*dy, antenna_x-k*dx] = 1
                        k += 1
    return antinode_map

with open('AOC_2024/day8.txt', 'r') as f:
    input_map =  [[x for x in line.strip()] for line in f.readlines()]

antinode_map = np.zeros([len(input_map), len(input_map[0])])
antinode_map1 = antinode_map.copy()
antinode_map2 = antinode_map.copy()

for j in range(len(input_map)):
    for i in range(len(input_map[0])):
        if input_map[j][i] != '.':
            antinode_map1 = create_antinodes_p1(j, i, input_map, antinode_map1)
            antinode_map2 = create_antinodes_p2(j, i, input_map, antinode_map2)

part1_ans = np.sum(antinode_map1)
print(f"Part 1:", part1_ans)

part2_ans = np.sum(antinode_map2)
print(f"Part 2", part2_ans)