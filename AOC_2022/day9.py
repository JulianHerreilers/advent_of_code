file_name = "AOC/2022/data/aoc_9.txt"
with open(file_name) as file:
    data = [line.strip().split() for line in file]


def update_T(hx, tx, hy, ty, vists):
    d_x =  hx-tx
    d_y =  hy-ty
    x_sign = d_x>0 
    y_sign = d_y>0

    if abs(d_x)+abs(d_y) >=3:
        if x_sign: tx+=1
        else: tx-=1
        if y_sign: ty+=1
        else: ty-=1

    elif abs(d_x) >=2:
        tx+=d_x/2

    elif abs(d_y) >=2:
        ty+=d_y/2
    vists.add((tx,ty))
    return tx,ty,vists


hx,tx,hy,ty = 0,0,0,0
vists = set()
for i in data:
    if i[0]=="R":
        for i in range(int(i[1])):
            hx+=1
            tx,ty,vists = update_T(hx, tx, hy, ty, vists)


    elif i[0]=="L":
        for i in range(int(i[1])):
            hx-=1
            tx,ty,vists = update_T(hx, tx, hy, ty, vists)

    elif i[0]=="U":
        for i in range(int(i[1])):
            hy+=1
            tx,ty,vists = update_T(hx, tx, hy, ty, vists)

    elif i[0]=="D":
        for i in range(int(i[1])):
            hy-=1
            tx,ty,vists = update_T(hx, tx, hy, ty, vists)

print("Part 1")
print(len(vists))


def update_T_multi(hx, tx, hy, ty, vists,n):
    d_x =  hx-tx
    d_y =  hy-ty
    x_sign = d_x>0 
    y_sign = d_y>0

    if abs(d_x)+abs(d_y) >=3:
        if x_sign: tx+=1
        else: tx-=1
        if y_sign: ty+=1
        else: ty-=1

    elif abs(d_x) >=2:
        tx+=d_x/2

    elif abs(d_y) >=2:
        ty+=d_y/2

    if n==8:
        vists.add((tx,ty))
    return tx,ty,vists

hx, hy = 0,0
tails = [0]
for i in range(17):
    tails.append(0)

print(len(tails))
vists = set()
for i in data:
    if i[0]=="R":
        for i in range(int(i[1])):
            hx+=1
            tails[0],tails[1], vists = update_T_multi(hx, tails[0], hy, tails[1], vists,0)
            for j in range(1,9):
                tails[2*j], tails[2*j+1],vists = update_T_multi(tails[2*(j-1)], tails[2*j], tails[2*(j-1)+1], tails[2*j+1], vists, j)


    elif i[0]=="L":
        for i in range(int(i[1])):
            hx-=1
            tails[0],tails[1], vists = update_T_multi(hx, tails[0], hy, tails[1], vists,0)
            for j in range(1,9):
                tails[2*j], tails[2*j+1],vists = update_T_multi(tails[2*(j-1)], tails[2*j], tails[2*(j-1)+1], tails[2*j+1], vists, j)

    elif i[0]=="U":
        for i in range(int(i[1])):
            hy+=1
            tails[0],tails[1], vists = update_T_multi(hx, tails[0], hy, tails[1], vists,0)
            for j in range(1,9):
                tails[2*j], tails[2*j+1],vists = update_T_multi(tails[2*(j-1)], tails[2*j], tails[2*(j-1)+1], tails[2*j+1], vists, j)

    elif i[0]=="D":
        for i in range(int(i[1])):
            hy-=1
            tails[0],tails[1], vists = update_T_multi(hx, tails[0], hy, tails[1], vists,0)
            for j in range(1,9):
                tails[2*j], tails[2*j+1],vists = update_T_multi(tails[2*(j-1)], tails[2*j], tails[2*(j-1)+1], tails[2*j+1], vists, j)

print("Part 2")
print(len(vists))


