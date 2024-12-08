file_name = "AOC/2022/data/aoc_8.txt"
with open(file_name) as file:
    trees = [list(map(int, (x for x in line.strip()))) for line in file]

def part_1(trees):
    total = 0

    width = len(trees[0])
    length = len(trees)
    
    for i in range(length):
        for j in range(width):
            if i == 0 or i ==length-1 or j == 0 or j==width-1:
                total+=1
            else:
                other_trees = [[tree for tree in trees[i][:]],[tree[j] for tree in trees]]

                if other_trees[0][j] > max(other_trees[0][:j]) or other_trees[0][j] > max(other_trees[0][j+1:]):
                    total +=1
                elif other_trees[1][i] > max(other_trees[1][:i]) or other_trees[1][i] > max(other_trees[1][i+1:]):
                
                    total +=1

    return total

def part_2(trees):
    total = 0

    width = len(trees[0])
    length = len(trees)
    best = 0
    
    for i in range(length):
        
        for j in range(width):
    # for i in range(3,4):
        
    #     for j in range(2,3):
            ans = [0,0,0,0]
            other_trees = [[tree for tree in trees[i][:]],[tree[j] for tree in trees]]
            # print(f"i{i}j{j}")
            # print(other_trees)

            if i != 0:
                for k in range(0,i):
                    if other_trees[1][i] > other_trees[1][i-k-1]:
                        ans[0] +=1
                    elif other_trees[1][i] <= other_trees[1][i-k-1]:
                        ans[0] +=1
                        break
            
            if i != length-1:
                for k in range(i+1,width):
                    if other_trees[1][i] > other_trees[1][k]:
                        ans[1] +=1
                    elif other_trees[1][i] <= other_trees[1][k]:
                        ans[1] +=1
                        break
                    
            if j != 0:
                for k in range(0,j):
                    if other_trees[0][j] > other_trees[0][j-k-1]:
                        ans[2] +=1
                    elif other_trees[0][j] <= other_trees[0][j-k-1]:
                        ans[2] +=1
                        break
                
            if j != width-1:
                for k in range(j+1,width):
                    if other_trees[0][j] > other_trees[0][k]:
                        ans[3] +=1
                    elif other_trees[0][j] <= other_trees[0][k]:
                        ans[3] +=1
                        break

            best = max(best, ans[0]*ans[1]*ans[2]*ans[3])

    return best

print(f"Part 1: {part_1(trees)}")
print(f"Part 2: {part_2(trees)}")
