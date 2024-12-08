file_name = "AOC/2022/data/aoc_4.txt"

with open(file_name) as file:
    data = [line.strip() for line in file]
counts_p1 = 0
counts_p2 = 0
for i in data:
    i = i.replace("-",",")
    i = i.split(",")

    a = set(range(int(i[0]), int(i[1])+1))
    b = set(range(int(i[2]), int(i[3])+1))  
    # if a.issubset(b) or b.issubset(a):
    #     counts_p1+=1
    # if set(a).intersection(b) or b.intersection(a):
    #     counts_p2+=1
    a = [int(i[0]),int(i[1])]
    b = [int(i[2]),int(i[3])]
    print(i)
    if (a[0]>=b[0] and a[1]<=b[1]) or (b[0]>=a[0] and b[1]<=a[1]):
        counts_p1+=1
    if (a[1]>=b[0] and a[0]<=b[0]) or (b[1]>=a[0] and b[0]<=a[0]):
        counts_p2+=1
print(counts_p1)
print(counts_p2)