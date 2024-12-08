file_name = "AOC/2022/data/aoc_11.txt"

from math import floor,prod, lcm
with open(file_name) as file:
    data = [line.strip().replace(":","").replace(",","").split() for line in file if len(line.strip().split())!=0]

print(data)
monkeys = [[],[],[],[]]
monkeys_inspects = [0,0,0,0]
monkeys = [[],[],[],[],[],[],[],[]]
monkeys_inspects = [0,0,0,0,0,0,0,0]
test_cases = []
for i in range(len(data)//6):
    # print(data[6*i+1][2:])
    for k in range(2,len(data[6*i+1])):
        monkeys[int(data[6*i][-1])].append(data[6*i+1][k])
    test_cases.append(int(data[i*6+3][-1]))
rounds = 20
round_to_check = [1,20,1000]
multiples = lcm(*[i for i in test_cases])


for l in range(rounds):
    m=0
    for i in range(len(monkeys)):
        for j in range(len(monkeys[i])):
            monkeys_inspects[i]+=1
            item = int(monkeys[i].pop(0))
            if data[m*6+2][-2]=="*": 
                if data[m*6+2][-1]=="old": item *=item
                else: item = item * int(data[m*6+2][-1])
            else: 
                if data[m*6+2][-1]=="old": item +=item
                else: item = item + int(data[m*6+2][-1])
            item = floor(item//3)
            # item = item%int(data[m*6+3][-1])
            # item = item%(3*int(data[m*6+3][-1]))
            if item%int(data[m*6+3][-1])==0: monkeys[int(data[m*6+4][-1])].append(item)
            else: 
                monkeys[int(data[m*6+5][-1])].append(item)

        m+=1
    # i+=6
print("Part 1")
print(monkeys)
print(monkeys_inspects)
monkeys_inspects.sort()
print(monkeys_inspects[-1]*monkeys_inspects[-2])


monkeys = [[],[],[],[]]
monkeys_inspects = [0,0,0,0]

monkeys = [[],[],[],[],[],[],[],[]]
monkeys_inspects = [0,0,0,0,0,0,0,0]

for i in range(len(data)//6):
    # print(data[6*i+1][2:])
    for k in range(2,len(data[6*i+1])):
        monkeys[int(data[6*i][-1])].append(data[6*i+1][k])
rounds = 10000
round_to_check = [1,20,1000]

for l in range(rounds):
    m=0
    for i in range(len(monkeys)):
        for j in range(len(monkeys[i])):
            monkeys_inspects[i]+=1
            item = int(monkeys[i].pop(0))
            if data[m*6+2][-2]=="*": 
                if data[m*6+2][-1]=="old": item *=item
                else: item = item * int(data[m*6+2][-1])
            else: 
                if data[m*6+2][-1]=="old": item +=item
                else: item = item + int(data[m*6+2][-1])
            # item = floor(item%3)
            # item = item%int(data[m*6+3][-1])
            item = item%multiples
            if item%int(data[m*6+3][-1])==0: monkeys[int(data[m*6+4][-1])].append(item)
            else: 
                monkeys[int(data[m*6+5][-1])].append(item)

        m+=1
    if l+1 in round_to_check:
        print(monkeys_inspects)
    # i+=6
monkeys_inspects.sort()
# print(monkeys_inspects)
print("Part 2")
print(monkeys_inspects[-1]*monkeys_inspects[-2])