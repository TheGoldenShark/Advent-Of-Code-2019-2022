with open("input.txt","r") as f: data=f.read().splitlines()
d = [[x.split(" ")[0], int(x.split(" ")[1])] for x in data]
sign = lambda x : -1 if x < 0 else 1
K = [[0,0] for x in range(10)]
pasPos = set()
pasPos.add('-'.join(map(str,K[-1])))
for i in d:
    for k in range(i[1]):
        if i[0] == 'U':
            K[-1][0] -=1
        elif i[0] == 'D':
            K[-1][0] +=1
        elif i[0] == 'L':
            K[-1][1] -= 1
        elif i[0] == 'R':
            K[-1][1] += 1

        for j in reversed(range(9)):
            d = [K[j+1][0] - K[j][0], K[j+1][1] - K[j][1]]
            if abs(d[0]) > 1 and d[1] == 0:
                K[j][0] += sign(d[0])
            elif d[0] == 0 and abs(d[1]) > 1:
                K[j][1] += sign(d[1])
            elif abs(d[0]) > 1 or abs(d[1]) > 1:
                K[j][0] += sign(d[0])
                K[j][1] += sign(d[1])

        pasPos.add('-'.join(map(str,K[0])))

    
print(len(pasPos))