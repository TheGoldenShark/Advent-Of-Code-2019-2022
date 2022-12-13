with open("input.txt","r") as f: data=f.read().splitlines()
d = [[x.split(" ")[0], int(x.split(" ")[1])] for x in data]
sign = lambda x : -1 if x < 0 else 1
H = [0,0]
T = [0,0]
pasPos = set()
pasPos.add('-'.join(map(str,T)))
for i in d:
    for k in range(i[1]):
        if i[0] == 'U':
            H[0] -=1
        elif i[0] == 'D':
            H[0] +=1
        elif i[0] == 'L':
            H[1] -= 1
        elif i[0] == 'R':
            H[1] += 1
        d = [H[0] - T[0], H[1] - T[1]]
        if abs(d[0]) > 1 and d[1] == 0:
            T[0] += sign(d[0])
        elif d[0] == 0 and abs(d[1]) > 1:
            T[1] += sign(d[1])
        elif abs(d[0]) > 1 or abs(d[1]) > 1:
            T[0] += sign(d[0])
            T[1] += sign(d[1])
        pasPos.add('-'.join(map(str,T)))

    
print(len(pasPos))