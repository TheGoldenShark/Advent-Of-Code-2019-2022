with open("input.txt","r") as f: data=f.readlines()
d = [[x[0],x[2]] for x in data] 
points = 0
beats = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
 }

score = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
 }
same = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

for i in d:
    if same[i[0]] == i[1]:
        points += 3
    elif beats[i[0]] == i[1]:
        points +=6
    else:
        points +=0  
    points += score[i[1]]

print(points)
