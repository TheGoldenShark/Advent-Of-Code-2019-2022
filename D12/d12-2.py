with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [list(x) for x in data]
S = []
E = []
starts = []
for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] == 'S':
            S = [i,j]
            starts.append(S)
        elif d[i][j] == 'E':
            E = [i,j]
        elif d[i][j] == 'a':
            starts.append([i,j])
stack = [S]
d[S[0]][S[1]] = 'a'
d[E[0]][E[1]] = 'z'
hash = lambda x : '-'.join(map(lambda p : str(p), x))

frontiers = [[x] for x in starts]
newFrontiers = [[] for x in starts]
visiteds = [set([hash(S)]) for x in starts]
turn = 0
eFound = False
while True:
    for f in range(len(frontiers)):
        newFrontiers[f] = []
        for i in frontiers[f]:
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
                if hash(j) not in visiteds[f]:
                    newFrontiers[f].append(j)
                    visiteds[f].add(hash(j))
        frontiers[f] = list(newFrontiers[f])
        if hash(E) in visiteds[f]:
            eFound = True
            break
    turn+=1
    if eFound:
        break
print(turn)
