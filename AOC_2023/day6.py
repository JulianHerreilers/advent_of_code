import re
from string import punctuation
from tqdm import tqdm
import numpy as np

def part1(filepath):
    ans = []
    with open(filepath) as file:
        data  = file.readlines()

    time = list(map(int, data[0].split()[1:]))
    dist = list(map(int, data[1].split()[1:]))

    for t,d in tqdm(zip(time, dist)):
        n = 0
        for i in range(0,t):
            if (t-i)*i>d: n+=1
        ans.append(n)

    print(ans)
    return np.prod(ans)


def part2(filepath):
    ans = []
    with open(filepath) as file:
        data  = file.readlines()

    time = int(''.join(data[0].split()[1:]))
    dist = int(''.join(data[1].split()[1:]))

    n = 0
    for i in range(0,time):
        if (time-i)*i>dist: n+=1
    ans.append(n)

    print(ans)
    return np.prod(ans)
    
def main():
    file_name = "data/day6.txt"

    print(f"Part 1 answer: {part1(file_name)}")
    print(f"Part 2 answer: {part2(file_name)}")

    # Part two I will be following the approach from https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py
    # I plan to use this as a way to improve the manner in which I read in my text inputs

    # print(f"Part 2 answer: {part2(file_name)}")

if __name__ == "__main__":
    main()