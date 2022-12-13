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
visited = set()
paths = []
minLen = 10000000

hash = lambda x : ','.join(['-'.join(map(lambda p : str(p), y)) for y in x])
dist = lambda x : (x[0] - E[0]) ** 2 + (x[1] - E[1]) ** 2

while len(stack) != 0:
    if (stack[-1] == E):
        minLen = min(minLen, len(stack)-1)
        visited.add(hash(stack))
        stack.pop()
        print("E Found")
        continue

    if len(stack) - 1 >= minLen:
        visited.add(hash(stack))
        stack.pop()
        continue

    moves = []
    if stack[-1][0] != 0 and (ord(d[stack[-1][0]][stack[-1][1]]) - ord(d[stack[-1][0] - 1][stack[-1][1]])) >= -1:
        moves.append([stack[-1][0] - 1, stack[-1][1]])
    if stack[-1][0] != (len(d) - 1) and (ord(d[stack[-1][0]][stack[-1][1]]) - ord(d[stack[-1][0] + 1][stack[-1][1]])) >= -1:
        moves.append([stack[-1][0] + 1, stack[-1][1]])
    if stack[-1][1] != 0 and (ord(d[stack[-1][0]][stack[-1][1]]) - ord(d[stack[-1][0]][stack[-1][1] - 1])) >= -1:
        moves.append([stack[-1][0], stack[-1][1] - 1])
    if stack[-1][1] != (len(d[0]) - 1) and (ord(d[stack[-1][0]][stack[-1][1]]) - ord(d[stack[-1][0]][stack[-1][1] + 1])) >= -1:
        moves.append([stack[-1][0], stack[-1][1] + 1])
    moved = False
    moves.sort(key = dist)
    for i in moves:
        if hash(stack + [i]) not in visited and i not in stack:
            stack.append(i)
            moved = True
            break
    if not moved:
        visited.add(hash(stack))
        stack.pop()
    

print(minLen)
# print(hash(stack))

