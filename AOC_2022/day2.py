file_name = "AOC/data/aoc_2.txt"
f = open(file_name, "r")
data = f.readlines()
f.close()
opp = ["A", "B", "C"]
me = ["X", "Y", "Z"]
score = 0 
# for i in data:
#     i = i.replace("\n","")
#     i = i.split()
#     if me.index(i[1]) == opp.index(i[0]):
#         score += (3 + me.index(i[1])+1)
#     if ((i[0]==opp[0] and i[1]==me[1]) or (i[0]==opp[1] and i[1]==me[2]) or (i[0]==opp[2] and i[1]==me[0])):
#         score +=(6 + me.index(i[1])+1)
#     if ((i[0]==opp[0] and i[1]==me[2]) or (i[0]==opp[1] and i[1]==me[0]) or (i[0]==opp[2] and i[1]==me[1])):
#         score +=(0 + me.index(i[1])+1)
for i in data:
    i = i.replace("\n","")
    i = i.split()
    if i[-1] == me[0]: #L
        if opp.index(i[0]) == 0:
            score +=(3)
        else:
            score +=(opp.index(i[0]))
    
    elif i[-1] == me[1]: #D
        score += (3 + opp.index(i[0])+1)

    elif i[-1] == me[2]: #W
        if opp.index(i[0]) == (len(opp)-1):
            score +=(6 + 1)
        else:
            score +=(6 + opp.index(i[0])+2)

print(score)