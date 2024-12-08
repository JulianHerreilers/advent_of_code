file_name = "AOC/AOC_2022/data/aoc_6.txt"
with open(file_name) as file:
    data = file.readline().strip()
num = 0
unique = 0
present = []
for i in range(len(data)):
    if len(set(data[i:i+4]))==4:
        print(i+4)
        break

for i in range(len(data)):
    if len(set(data[i:i+14]))==14:
        print(i+14)
        break
