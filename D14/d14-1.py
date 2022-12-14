with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [[(int(y.split(',')[0]), int(y.split(',')[1])) for y in x.split(" -> ")] for x in data]

rocks = set()
maxY = 0
for i in d:
    for k in range(len(i)):
        if k == 0:
            s = k
        else:
            if i[s][0] == i[k][0]:
                for j in range(min(i[s][1],i[k][1]), max(i[s][1],i[k][1]) + 1):
                    rocks.add((i[s][0], j))
                    maxY = max(maxY, j)
                s = k
            elif i[s][1] == i[k][1]:
                for j in range(min(i[s][0],i[k][0]), max(i[s][0],i[k][0]) + 1):
                    rocks.add((j, i[s][1]))
                    maxY = max(maxY, i[s][1])
                s = k

sand = (500,0)
sands = set()
while True:
    if sand[1] > maxY:
        break
    if (sand[0], sand[1] + 1) not in rocks and (sand[0], sand[1] + 1) not in sands:
        sand = (sand[0], sand[1] + 1)
    elif (sand[0] - 1, sand[1] + 1) not in rocks and (sand[0] - 1, sand[1] + 1) not in sands:
        sand = (sand[0] - 1, sand[1] + 1)
    elif (sand[0] + 1, sand[1] + 1) not in rocks and (sand[0] + 1, sand[1] + 1) not in sands:
        sand = (sand[0] + 1, sand[1] + 1)
    else:
        sands.add(sand)
        sand = (500,0)
    
print(len(sands))