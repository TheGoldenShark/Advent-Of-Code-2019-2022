with open("input.txt","r") as f: data=f.readlines()
d = [[x[0],x[2]] for x in data] 
points = 0
beats = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
 }

same = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

loses = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
}

score = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
 }


for i in d:
    if i[1] == 'X':
        pick = loses[i[0]]
    elif i[1] == 'Y':
        pick = same[i[0]]
    else:
        pick = beats[i[0]]

    if same[i[0]] == pick:
        points += 3
    elif beats[i[0]] == pick:
        points +=6
    else:
        points +=0  
    points += score[pick]

print(points)
