with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [list(x) for x in data]
S = []
E = []
for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] == 'S':
            S = [i,j]
        if d[i][j] == 'E':
            E = [i,j]
stack = [S]
d[S[0]][S[1]] = 'a'
d[E[0]][E[1]] = 'z'
hash = lambda x : '-'.join(map(lambda p : str(p), x))

frontier = [S]
newFrontier = []
visited = set([hash(S)])
turn = 0
while True:
    newFrontier = []
    for i in frontier:
        moves = []
        if i[0] != 0 and (ord(d[i[0]][i[1]]) - ord(d[i[0] - 1][i[1]])) >= -1:
            moves.append([i[0] - 1, i[1]])
        if i[0] != (len(d) - 1) and (ord(d[i[0]][i[1]]) - ord(d[i[0] + 1][i[1]])) >= -1:
            moves.append([i[0] + 1, i[1]])
        if i[1] != 0 and (ord(d[i[0]][i[1]]) - ord(d[i[0]][i[1] - 1])) >= -1:
            moves.append([i[0], i[1] - 1])
        if i[1] != (len(d[0]) - 1) and (ord(d[i[0]][i[1]]) - ord(d[i[0]][i[1] + 1])) >= -1:
            moves.append([i[0], i[1] + 1])
        for j in moves:
            if hash(j) not in visited:
                newFrontier.append(j)
                visited.add(hash(j))
    frontier = list(newFrontier)
    turn+=1               
    if hash(E) in visited:
        print(turn)
        break
