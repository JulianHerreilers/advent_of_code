file_name = "AOC/2020/data/aoc_1.txt"

with open(file_name) as file:
    data = [line.strip() for line in file]

for i in range(len(data)):
    for j in range(len(data)):
        if (int(data[i])+int(data[j])==2020) and i!=j:
            print (int(data[i])*int(data[j]))
            break

for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if (int(data[i])+int(data[j])+int(data[k])==2020) and i!=j and k!=j and i!=k:
                print (int(data[i])*int(data[j])*int(data[k]))
                break
                
