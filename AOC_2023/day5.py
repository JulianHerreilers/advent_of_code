import re
from string import punctuation
from tqdm import tqdm
import numpy as np
from math import ceil

### Working method for test case but does not work for long numbers
def part1_old(data):
    ans = 0
    seeds = {seed:[int(seed)] for seed in data[0][1:]}
    i = 1
    mapping = {}
    for i in tqdm(range(2, len(data))):
        if len(data[i])>0 and data[i][0][0].isdigit():
            for j in range(0, int(data[i][-1])):
                mapping[str((int(data[i][1])+j))] = int(data[i][0])+j
              
        elif len(data[i])==0 or i == len(data):
            x,a,y = data[i+1][0].split("-")
            print(f"current seed arrangement: {seeds}")
            for seed in seeds.keys():
                
                if str(seeds[seed][-1]) in mapping.keys():
                    seeds[seed].append(int(mapping[str(seeds[seed][-1])]))
                else:
                    seeds[seed].append(seeds[seed][-1])
            mapping = {}

        print(f"current seed arrangement: {seeds}")
        i+=1

    locations = [seeds[seed][-1] for seed in seeds.keys()]
    ans = min(locations)
    return ans

def par2_old(data):
    seeds = [int(seed) for seed in data[0][1::2]]
    total_seeds = 0
    ranges = [[np.inf, -np.inf]]
    for i in range(0, ceil(len(data[0])//2)):
        total_seeds += int(data[0][2*i+2])
        xmin = int(data[0][1+2*i])
        xmax = int(data[0][1+2*i]) + int(data[0][2*i+2]) - 1
        valid = 1
        for j in range(len(ranges)):
            x1,x2 = ranges[j][0],ranges[j][1]
            # print(f"x1 is {x1} and x2 is {x2} and xmin is {xmin} and xmax is {xmax}")
            if xmin >= x1 and xmax<=x2: 
                valid = 0
                break
            elif xmin <=x1 and xmax>=x2: 
                ranges[j]= [xmin, xmax]
                valid = 0
                break
            elif xmin <=x1 and xmax<=x2 and xmax>=x1:
                ranges[j]= [xmin, x2] 
                valid = 0
                break
            elif xmin >=x1 and xmax>=x2 and xmin<=x2:
                ranges[j]= [x1, xmax] 
                valid = 0
                break
        if valid==1:
            ranges.append([xmin, xmax])
            
        Total_ranges = sum([x[-1]-x[0]+1 for x in ranges])
        # if min_x
    print(f"Ranges is: {ranges}")
    ans = 0
    print(f"Total seeds is: {total_seeds}")
    print(f"Total seeds to check using optimization is: {Total_ranges}")
    return ans

def part1(data):
    ans = 0
    seeds = {seed:[int(seed)] for seed in data[0][1:]}
    i = 1
    mapping = []
    for i in tqdm(range(2, len(data))):
        if len(data[i])>0 and data[i][0][0].isdigit():
            mapping.append(data[i])
            
        elif len(data[i])==0 or i == len(data):
            # print(f"Mapping is {mapping}")
            x,a,y = data[i+1][0].split("-")
            # i += 2
            # current_map = {}
            # print(f"Mapping from {x} to {y}")
            # print(f"current seed arrangement: {seeds}")
            for seed in seeds.keys():
                for m in mapping:
                    
                    if seeds[seed][-1]>=int(m[1]) and seeds[seed][-1]<int(m[1])+int(m[-1]):

                        seeds[seed].append(int(m[0])-int(m[1])+seeds[seed][-1])
                        break
                else:
                    seeds[seed].append(seeds[seed][-1])
            mapping = []
        # i+=1
    
    for seed in seeds.keys():
        for m in mapping:
            
            if seeds[seed][-1]>=int(m[1]) and seeds[seed][-1]<int(m[1])+int(m[-1]):
                # print(f"source m1:{m[1]} destination m0:{m[0]} range m2:{m[-1]}")
                # print(f"Seed {seed} mapping {seeds[seed][-1]} to {int(m[0])-int(m[1])+seeds[seed][-1]}")
                seeds[seed].append(int(m[0])-int(m[1])+seeds[seed][-1])
                break
        else:
            seeds[seed].append(seeds[seed][-1])




    locations = [seeds[seed][-1] for seed in seeds.keys()]
    print(locations)
    ans = min(locations)
    print(seeds)
    return ans

def part2_augmented_incorrect(data):

    # Credits to https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py for helping me
    # realise I have to break the ranges up into segments and save the specific mappings
    seeds = []
    new_mapping = 0
    ans = 0
    for i in range(0, ceil(len(data[0])//2)):
        seeds.append([int(data[0][1+2*i]),int(data[0][1+2*i]) + int(data[0][2*i+2])])

    mapping = []
    print(f"Seeds are: {seeds} with len {len(seeds)}")
    print(len(data[-1]))
    for i in tqdm(range(2, len(data))):
        # print(i)
        if len(data[i])>0 and data[i][0][0].isdigit():
            mapping.append(list(map(int, data[i])))
            # print(f"Mapping before processing is of length {len(mapping)} and is {mapping}")
        
        elif len(data[i])==0 or i == len(data):
        # else:
            # x,a,y = data[i+1][0].split("-")
            # print(f"Mapping from {x} to {y}")
            # print(f"current mapping is {mapping}")
            new_mapping = []
            while len(seeds)>0:
                s_start,s_end = seeds.pop()
                for dest, src, ranges in mapping:
                    # dest, src, ranges = m

                    # Check for overlap
                    overlap_start = max(s_start, src)
                    overlap_end = min(s_end, src+ranges)

                    # Map to next map
                    if overlap_start < overlap_end:
                        new_mapping.append([overlap_start - src + dest, overlap_end - src + dest])

                        # Now we need to account for remained sections to ensure they do not get discarded:
                        if overlap_start > s_start:
                            new_mapping.append([s_start, overlap_start])

                        if s_end > overlap_end:
                            new_mapping.append([overlap_end, s_end])
                        break

                # Else carry seed segments to existing new mapping as not in a mapping range
                else:
                    new_mapping.append([s_start, s_end])

            seeds = new_mapping # Passing next layer mapping on
            # print(f"New mapping: {seeds}")
            mapping = []
        

        


            # print(f"Mapping is {mapping}")
            # x,a,y = data[i+1][0].split("-")
            # i += 2
            # current_map = {}
            # print(f"Mapping from {x} to {y}")
            # print(f"current seed arrangement: {seeds}")

    print(min(seeds)[0])
    return min([seed[0] for seed in seeds])


def part2(filepath):
    # Credits to https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py for helping me
    # realise I have to break the ranges up into segments and save the specific mappings and for the approach of this question
    answer = 0
    with open(filepath) as file:
        data, *data_blocks = file.read().split("\n\n")

    data = list(map(int, data.split(":")[1].split()))
    seeds = [(data[2*i], data[2*i]+data[2*i+1]) for i in range(0, ceil(len(data)/2))]
    # print(f"Seeds are {seeds}")

    for mapping in data_blocks:
        data_map = []
        for map_range in mapping.splitlines()[1:]: # [1:] ignores the initial title of the map
            # dest, src, ranges = 
            data_map.append(list(map(int, map_range.split())))

        # Now we process the mapping based on the seeds
            
        new_mapping = []
        while len(seeds)>0:
            s_start,s_end = seeds.pop()
            # print(f"sstart: {s_start}, send:{s_end}")
            for mapping in data_map:
                dest, src, ranges  = mapping


                # Check for overlap
                overlap_start = max(s_start, src)
                overlap_end = min(s_end, src+ranges)

                # Map to next map
                if overlap_start < overlap_end:
                    new_mapping.append((overlap_start - src + dest, overlap_end - src + dest))

                    # Now we need to account for remained sections to ensure they do not get discarded:
                    # These need to be added to the seeds and not new mapping - bug which cost me a lot of time
                    if overlap_start > s_start:
                        seeds.append((s_start, overlap_start))

                    if s_end > overlap_end:
                        seeds.append((overlap_end, s_end))
                    break
            
            # Else carry seed segments to existing new mapping as not in a mapping range
            else:
                new_mapping.append((s_start, s_end))

        seeds = new_mapping # Passing next layer mapping on

    return min([seed[0] for seed in seeds])
    
def main():
    file_name = "data/day5.txt"
# seeds: 79 14 55 13
    with open(file_name) as f:
        data = f.readlines()
    
    refined_data =[line.replace("\n","").split() for line in data]
    print(f"Part 1 answer: {part1(refined_data)}")

    # Part two I will be following the approach from https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py
    # I plan to use this as a way to improve the manner in which I read in my text inputs

    print(f"Part 2 answer: {part2(file_name)}")
    print(f"Part 2 correct answer: 57451709")
    print(f"For part 2: 56146061 is not valid as too low")
    print(f"For part 2: 241075781 is not valid as too high")

if __name__ == "__main__":
    main()