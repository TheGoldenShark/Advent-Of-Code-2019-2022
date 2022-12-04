with open("input.txt","r") as f: data=f.read().splitlines()
d = [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in data]
count = 0
for i in d:
    if (i[0][0] >= i[1][0] and i[0][0] <= i[1][1]) or (i[1][0] >= i[0][0] and i[1][0] <= i[0][1]): count+=1
print(count)