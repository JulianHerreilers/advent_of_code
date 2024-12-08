import numpy as np
import re
data = []

with open('AOC_2024/day3.txt', 'r') as f:
    lines = "".join(x for x in f.readlines())

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
part1 = 0
for i, match in enumerate(matches):
    x = list(map(int, match[4:-1].split(",")))
    part1 += x[0]*x[1]
print(part1)

# lines = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
matches_p2 = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", lines)
part2 = 0
active=True

for i in range(len(matches_p2)):
    newloop = True
    curr = matches_p2[i]
    if 'do()' in curr: 
        active =  True
        newloop = False
    elif 'don\'t()' in curr: active = False
    
    if active and newloop:

        x = list(map(int, matches_p2[i][4:-1].split(",")))
        part2 += x[0]*x[1]

print(part2)
