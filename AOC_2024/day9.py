from tqdm import tqdm
import numpy as np
from tqdm import tqdm
with open('AOC/AOC_2024/data/day9.txt', 'r') as f:
    data =  [int(x) for x in f.readline()]

output=[]
num = 0
for i in range(0, len(data)):
    if data[i]!=0:
        if (i+1)%2:
            output. extend(str(num) for i in range(0, data[i]))
            num+=1
        else:
            output. extend('.' for i in range(0, data[i]))


idx = len(output)-1
reordered_output = output.copy()
for i in range(len(reordered_output)):
    if reordered_output[i] == '.':

        for j in range(idx, i, -1):
            if reordered_output[j] != '.':
                temp = reordered_output[j]
                reordered_output[j] = reordered_output[i]
                reordered_output[i] = temp
                # print(f"Swapped:{reordered_output[i],reordered_output[j], reordered_output}, i:{i}, j:{j}")
                idx = j
                break

print(data)
print(output)
print(reordered_output)
part1_ans = 0
for i in range(len(output)):
    if reordered_output[i]==".":
        break
    else:
        part1_ans += int(reordered_output[i])*i
print(f"Part 1:", part1_ans)

# Part 1 faster -  thanks to HyperNeutrino for the guidelines
with open('AOC/AOC_2024/data/day9.txt', 'r') as f:
    data =  [int(x) for x in f.readline()]

output=[]
num = 0
for i in range(0, len(data)):
    if data[i]!=0:
        if (i+1)%2:
            output. extend(num for i in range(0, data[i]))
            num+=1
        else:
            output. extend([-1 for i in range(0, data[i])])

blanks = [i for i,x in enumerate(output) if x == -1]

for idx in blanks:
    while output[-1] == -1: output.pop()
    if len(output) <=  idx:
        break # break out of loop if removed all trailing blanks
    output[idx] = output.pop() # replace blank with last number in array

print(data)
print(output)
part1_ans = 0
for i in range(len(output)):
    if output[i]==-1:
        break
    else:
        part1_ans += output[i]*i
print(f"Part 1:", part1_ans)

files = {}
blanks = []
num = 0
entry_idx = 0
for i in range(0, len(data)):
    if data[i]!=0:
        if (i+1)%2:
            files[num] = (entry_idx, data[i])
            num+=1 
        else:
            blanks.append((entry_idx, data[i]))
    entry_idx += data[i]

#Starting with the files in reverse
print(files)
while num > 0:
    num -=1
    file_pos, num_files = files[num]

    for i,(blank_pos, num_blanks) in enumerate(blanks):
        if blank_pos < file_pos:
            if num_blanks >= num_files:
                files[num] = (blank_pos, num_files)
                if num_blanks == num_files: blanks.pop(i)
                else: blanks[i] = (blank_pos+num_files, num_blanks-num_files)
                break

print(files)
part2_ans = 0
for id, (start_idx, num_files) in files.items():
    for pos in range(start_idx, start_idx+num_files):
        part2_ans += pos*id

print(f"Part 2:", part2_ans)