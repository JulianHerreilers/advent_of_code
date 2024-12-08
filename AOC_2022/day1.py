file_name = "AOC/data/aoc_1.txt"
f = open(file_name, "r")
data = f.readlines()
f.close()
ans = []
cal = 0
maxes = []
for i in data:
    if i == '\n':
        ans.append(cal)
        cal = 0
    else:
        
        cal += int(i.replace('\n',""))

for j in range(3):
    maxes.append(max(ans))
    for i in range(len(ans)):
        if ans[i] == maxes[-1]:
            ans[i] = 0
print(maxes)    
print(sum(maxes))


