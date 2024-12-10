from tqdm import tqdm
import numpy as np
from tqdm import tqdm

directions = [(-1,0), (1,0), (0,1), (0,-1)] # U, D, R, L


def get_trailhead_score(y, x, rows, cols, input_map):
    total_score = 0
    available_steps = [(y, x)]
    peaks_tracker = []
    while available_steps:
        curr_y, curr_x = available_steps.pop(0)
        for dir in directions:
            d_y, d_x = dir
            next_y, next_x = curr_y+d_y, curr_x+d_x
            if 0<= next_y < rows and  0<= next_x < cols:
                if input_map[next_y][next_x] - input_map[curr_y][curr_x] == 1:
                    available_steps.append((next_y, next_x))

                if input_map[next_y][next_x] == 9 and input_map[next_y][next_x] - input_map[curr_y][curr_x] == 1:
                    peaks_tracker.append((next_y, next_x))
        
    return peaks_tracker

data = []
with open('AOC_2024/data/day10.txt', 'r') as f:
    for line in f.readlines():
        data.append([int(x) for x in line.strip()])

rows = len(data)
cols = len(data[0])

start_points_map = [(j,i) for j in range(rows)  for i in range(cols) if data[j][i] == 0]

part1_ans = 0
part2_ans = 0

for (y,x) in start_points_map:
    target_routes =  get_trailhead_score(y, x, rows, cols, data) # list of all summits

    part1_ans += len(set(target_routes)) # list of only distinct summits
    part2_ans += len(target_routes)
        
print(f"Part 1:", part1_ans) 
print(f"Part 2:", part2_ans) 