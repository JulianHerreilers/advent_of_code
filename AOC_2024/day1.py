import numpy as np
with open('AOC_2024/day1.txt', 'r') as f:
    data = f.readlines()

col1, col2 = [], []
for line in data:
    col1.append(int(line.split()[0]))
    col2.append(int(line.split()[1]))

sorted_1 = np.array(sorted(col1))
sorted_2 = np.array(sorted(col2))
total = np.sum(np.abs(sorted_1-sorted_2))
print(total)

from collections import Counter
counter_2 = Counter(sorted_2)

total = 0
for i in sorted_1:
    total += i*counter_2[i]
print(total)