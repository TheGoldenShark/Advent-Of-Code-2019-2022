with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input-2.txt","r") as f: data=f.read().splitlines()

def parseArrString(s):
    arr = []
    if len(s) == 0:
        return None
    if s[0] == '[':
        curItem = []
        n = 1
        pos = 1
        for pos in range(1, len(s)):
            if s[pos] == '[':
                n += 1
                curItem.append(s[pos])
            elif s[pos] == ']' and n == 1:
                arr.append(curItem)
                break
            elif s[pos] == ']' and n != 1:
                n -= 1
                curItem.append(s[pos])
            elif n == 1 and s[pos] == ',':
                arr.append(curItem)
                curItem = []
            else:
                curItem.append(s[pos])
        out = []
        for i in arr:
            p = parseArrString(i)
            if p is not None:
                out.append(parseArrString(i)) 
        return out
    else:
        return int(''.join(s))

def ordered (l, r):
    if type(l) is int and type(r) is int:
        if l == r:
            return -1
        return l < r
    else:
        if type(l) == int: l = [l]
        if type(r) == int: r = [r]

        for i in range(min(len(l), len(r))):
            val = ordered(l[i], r[i])
            if val != -1:
                return val
        if len(l) == len(r):
            return  -1
        return len(l) < len(r)

l = []
r = []
p = 0
count = 0
for i in range(len(data) + 1):
    if (i % 3 == 0):
        l = parseArrString(data[i])
    elif ((i-1) % 3 == 0):
        r = parseArrString(data[i])
    elif ((i-2) % 3 == 0):
        order = ordered(l,r)
        if order == -1 or order:
            count += int(i/3) + 1

print(count)


