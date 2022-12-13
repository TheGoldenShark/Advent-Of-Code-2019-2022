with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [[]]
monkey = 0
for i in data:
    if i == '':
        d.append([])
        monkey +=1
        continue
    words = i.split(" ")
    if words[0] == "Monkey":
        continue
    elif words[2] == "Starting":
        d[monkey].append([int(x.replace(',','')) for x in words[4:]])
    elif words[2] == "Operation:":
        d[monkey].append([lambda x, y, z=words[6]: x * y if z == '*' else x + y, words[7]])
    elif words[2] == "Test:":
        d[monkey].append(lambda x, y=int(words[5]) : x % y == 0)
    elif words[4] == "If":
        d[monkey].append(int(words[9]))
    
    
    else:
        d[monkey].append(i)

inspections = [0 for x in d]
    
for i in range(20):
    for j in range(len(d)):
        k = 0
        while k < len(d[j][0]):
            d[j][0][k] = d[j][1][0](d[j][0][k], d[j][0][k] if d[j][1][1] == "old" else int(d[j][1][1]))
            inspections[j] += 1
            d[j][0][k] = int(d[j][0][k]/3)
            if d[j][2](d[j][0][k]):
                d[d[j][3]][0].append(d[j][0].pop(k))
            else:
                d[d[j][4]][0].append(d[j][0].pop(k))
print(sorted(inspections)[-1] * sorted(inspections)[-2])


