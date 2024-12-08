file_name = "AOC/2022/data/aoc_5.txt"

with open(file_name) as file:
    data = [line.strip().split() for line in file]
bins = [ ["S","L","W"], 
         ["J","T","N","Q"],
         ["S","C","H","F","J"],
         ["T","R","M","W","N","G","B"],
         ["T","R","L","S","D","H","Q","B"],
         ["M","J","B","V","F","H","R","L"],
         ["D","W","R","N","J","M"],
         ["B","Z","T","F","H","N","D","J"],
         ["H","L","Q","N","B","F","T"]]

bins2 = [["S","L","W"], 
         ["J","T","N","Q"],
         ["S","C","H","F","J"],
         ["T","R","M","W","N","G","B"],
         ["T","R","L","S","D","H","Q","B"],
         ["M","J","B","V","F","H","R","L"],
         ["D","W","R","N","J","M"],
         ["B","Z","T","F","H","N","D","J"],
         ["H","L","Q","N","B","F","T"]]

for k,i in enumerate(data):
    for j in range(int(i[1])):
        bins[int(i[5])-1].append(bins[int(i[3])-1].pop(-1))
s=""
for i in bins:
    s += i[-1]


for k,i in enumerate(data):
    temp = ""
    for j in range(int(i[1])):
        temp += bins2[int(i[3])-1].pop(-1)

    for l in temp[::-1]:
        bins2[int(i[5])-1].append(l)
        
s2=""
for i in bins2:
    s2 += i[-1]

print(s)
print(s2)

