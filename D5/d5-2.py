with open("input.txt","r") as f: data=f.read().splitlines()
stacks = [[] for x in range(int(len(data[0])/4)+1)]
for i in range(len(data)):
    if data[i][0] == ' ': break
    for k in range(int(len(data[i])/4)+1):
        pos = k*4 + 1
        if data[i][pos] != ' ': stacks[k].insert(0, data[i][pos])
for k in range(i+2, len(data)):
    str = data[k].split(' ')
    n = int(str[1])
    s = int(str[3])
    e = int(str[5])
    for j in range(n):
        stacks[e-1].append(stacks[s-1].pop(-n+j))
print(''.join([x[-1] for x in stacks]))
