with open("input.txt","r") as f: data=f.read().splitlines()
d = [x.split(' ') for  x in data]
dirSize = dict()

curDir = [""]
contents = [0]
lsExecuted = False
for i in d:
    if i[0] == "$":
        if lsExecuted:
            dirSize['/'.join(curDir)] = contents
            lsExecuted = False
        if i[1] == "cd" and i[2] == "/":
            curDir = [""]
        elif i[1] == "cd" and i[2] == "..":
            curDir.pop()
        elif i[1] == "cd":
            curDir.append(i[2])
        elif i[1] == "ls":
            lsExecuted = True
            contents = [0]
    else:
        if i[0] == "dir":
            contents.append(i[1])
        else:
            contents[0] += int(i[0])
if lsExecuted:
    dirSize['/'.join(curDir)] = contents
    lsExecuted = False

def getSize(t):
    contents = dirSize[t]
    size = 0
    for i in contents:
        if type(i) is int:
            size += i
        else:
            size += getSize('/'.join([t, i]))
    return size

minSize = 30000000 - (70000000 - getSize(""))
sizes = min([getSize(x) for x in dirSize.keys() if getSize(x) >= minSize])
print(sizes)