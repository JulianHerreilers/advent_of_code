import numpy as np
data = []
# with open('AOC_2024/day2test.txt', 'r') as f:
with open('AOC_2024/day2.txt', 'r') as f:
# with open('AOC_2024/day2list.txt', 'r') as f:
    for line in f.readlines():
        data.append(list(map(int, line.strip().split())))

part1_correct = 0
flag = 0
invalid_idxs = []
part1_valid_idxs = []

def check_safe(levels):
    safe = True
    ans = levels
    ordered = sorted(ans)
    # Check if monotonic
    if ans == ordered or ans[::-1] == ordered:
        # Check ranges
        for i in range(0, len(ans)-1):
            if np.abs(ans[i]-ans[i+1])>3 or np.abs(ans[i]==ans[i+1]):
                safe = False
                break
    else: return False
    return safe

for idx, ans in enumerate(data):
    flag = 0
    if check_safe(ans):
            part1_correct += 1
            part1_valid_idxs.append(idx)
    else: invalid_idxs.append(idx)

print(f"part 1:",part1_correct)
print(f" {len(part1_valid_idxs)} valid of {len(data)} for part 1")

part2_correct = 0
part2_valid_idxs = []
part2_invalid_idxs = []

for idx in invalid_idxs:
    recitfied_report = False
    
    ans = data[idx]

    for i in range(0, len(ans)):
        temp = ans.copy()
        temp.pop(i)
        if check_safe(temp):
            recitfied_report = True
    part2_correct += recitfied_report


print("part 1:",part1_correct, "part 2:", part2_correct, "total:", part1_correct+part2_correct)

# 493 is too high
