file_name = "AOC/2022/data/aoc_3.txt"

with open(file_name) as file:
    data = [line.strip() for line in file]
scores = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))

count = 0

for i in data:
    i = i.replace("\n","")
    n = len(i)
    a = set(i[:n//2])
    b = set(i[n//2:])
    c = a.intersection(b)
    count += scores.index(c.pop())+1
print(count)

count = 0
for i in range(0, len(data)//3):
    x = data[i*3]
    y = data[i*3 +1]
    z = data[i*3 +2]
    a = set(x)
    b = set(y)
    c = set(z)
    d = a.intersection(b,c)
    count += scores.index(d.pop())+1
print(count)
