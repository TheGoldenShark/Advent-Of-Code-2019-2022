with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [[int(y) for y in x] for x in data]
vis = [[False for y in x] for x in d]
for i in range(len(d)):
    maxLeft = -1
    maxRight = -1
    for k in range(len(d[i])):
        if d[i][k] > maxLeft:
            vis[i][k] = True
            maxLeft = d[i][k]
        if d[i][-(k+1)] > maxRight:
            vis[i][-(k+1)] = True
            maxRight = d[i][-(k+1)]

for i in range(len(d[0])):
    maxUp = -1
    maxDown = -1
    for k in range(len(d)):
        if d[k][i] > maxUp:
            vis[k][i] = True
            maxUp = d[k][i]
        if d[-(k+1)][i] > maxDown:
            vis[-(k+1)][i] = True
            maxDown = d[-(k+1)][i]

print(sum([sum(x) for x in vis]))