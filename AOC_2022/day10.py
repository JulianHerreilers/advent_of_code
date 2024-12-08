file_name = "AOC/2022/data/aoc_10.txt"
with open(file_name) as file:
    data = [line.strip().split() for line in file]

X = 1
cycles = 0
checkpoints = [20, 60, 100, 140, 180, 220]
CRI_cycles = [40, 80, 120, 160, 200, 240]
scores = [0,0,0,0,0,0]
updated = 0
CRI = ""

def check_checkpoints(cycles, checkpoints, X):
    if cycles in checkpoints:
        scores[checkpoints.index(int(cycles))] = cycles*X
        return True



for i in data:
    if i[-1]=="noop":
        cycles += 1
        check_checkpoints(cycles, checkpoints, X)
    else:
        for j in range(2):
            cycles +=1
            if check_checkpoints(cycles, checkpoints, X):
                updated = 1
        X += int(i[-1])
        if updated ==0:
            check_checkpoints(cycles, checkpoints, X)
        updated = 0

print("Part 1")
print(cycles)
print(X)
print(scores)
print(sum(scores))


X = 1
m=0
cycles = 0
checkpoints = [20, 60, 100, 140, 180, 220]
CRI_cycles = [39, 79, 119, 159, 199, 239]
scores = [0,0,0,0,0,0]
updated = 0
CRI = ""

def process_print(m,X,cycles, CRI):
    if X==cycles-m*40 or X-1==cycles-m*40 or X+1==cycles-m*40: 
            CRI += "#"
    else: CRI += "."
    if cycles in CRI_cycles: 
            m+=1
            CRI+="\n"
    return m,X,cycles, CRI

for i in data:
    if i[-1]=="noop":
        
        m,X,cycles, CRI=process_print(m,X,cycles, CRI)
        cycles += 1
        

        
    else:
        for j in range(2):
            
            m,X,cycles, CRI=process_print(m,X,cycles, CRI)
            cycles +=1
        
        X += int(i[-1])
    

print("Part 2")
print(CRI)