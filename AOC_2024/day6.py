import numpy as np
import re
import random
from tqdm import tqdm

guard_position = ()
guard_x, guard_y = 0, 0
v_y, v_x = 0, 0


guard_set_v = {'^':(-1,0), 'v':(1,0),'>':(0,1),'<':(0,-1)}
guard_change_d = {'^':'>', 'v':'<' ,'>':'v' ,'<':'^'}

with open('AOC_2024/day6.txt', 'r') as f:
    data =  [[x for x in line.strip()] for line in f.readlines()]

free_map = np.zeros([len(data), len(data[0])])
old_obst_map = np.zeros([len(data), len(data[0])])
new_obst_map = np.zeros([len(data), len(data[0])])

for j in range(len(data)):
    for i in range(len(data[j])):
        if data[j][i] not in ['#','.']:
            print(data[i][j])
            init_guard_y, init_guard_x = j,i

        # Part 2            
        elif data[j][i] == "#":
            old_obst_map[j,i] = 1
            
        elif data[j][i] == ".":
            free_map[j,i] = 1


guard_y, guard_x = init_guard_y, init_guard_x
init_guard_d = data[guard_y][guard_x]
guard_d = init_guard_d
v_y, v_x = guard_set_v[guard_d]
pos_map = np.zeros([len(data),len(data[0])])
pos_map[guard_y, guard_x] = 1
spots_travelled = []
guard_route =[]

while 0<= guard_x <= len(data[0]) or 0 <=guard_y <= len(data):
    if data[guard_y+v_y][guard_x+v_x] == '#':
        guard_d = guard_change_d[guard_d]
        v_y, v_x = guard_set_v[guard_d]
    else:
        guard_y, guard_x = guard_y+v_y, guard_x+v_x
        guard_route.append((guard_y, guard_x))
        pos_map[guard_y, guard_x] = 1
        if guard_y+v_y>= len(data) or guard_x+v_x >= len(data[0]): break
        else:  pos_map[guard_y, guard_x] = 1

part1_correct = np.sum(pos_map)
print('Part 1:', part1_correct)

print(np.sum(old_obst_map))
print(np.sum(free_map))


def check_loop(obst_y, obst_x, init_y, init_x, guard_d, old_obst_map, n_max_steps = 2*len(data)*len(data)):
    steps = 0
    old_obst_map[obst_y, obst_x] = 1
    guard_y, guard_x = init_y, init_x
    init_guard_d = guard_d
    v_y, v_x = guard_set_v[guard_d] 
    while 0<= guard_x <= len(data[0]) or 0 <=guard_y < len(data):
        steps += 1
        if old_obst_map[guard_y+v_y,guard_x+v_x]:
            guard_d = guard_change_d[guard_d]
            v_y, v_x = guard_set_v[guard_d]
        else:
            guard_y, guard_x = guard_y+v_y, guard_x+v_x
            if guard_y+v_y== len(data) or guard_y+v_y<0 or guard_x+v_x == len(data[0]) or guard_x+v_x <0: break
            
        if steps >= n_max_steps: return True
        if guard_y ==  init_y and guard_x ==  init_x and guard_d == init_guard_d: return True
    return False
    

print(init_guard_x, init_guard_x)
guard_d = data[init_guard_y][init_guard_x]



v_y, v_x = guard_set_v[init_guard_d]

remove_idx = 0
for k in range(len(guard_route)):
    if guard_route[k] == (init_guard_y,init_guard_x):
        remove_idx = k
        print("Initial is here")
guard_route.pop(remove_idx)

for (j,i) in tqdm(guard_route):
    ans = check_loop(j, i, init_guard_y, init_guard_x, guard_d, old_obst_map.copy() )
    if ans: new_obst_map[j,i] = 1


part2_correct = np.sum(new_obst_map)
print('Part 2:', part2_correct)

print(new_obst_map)
        

# 4449 is too high

# 1720

# 14263 is WAY TOO HIGH