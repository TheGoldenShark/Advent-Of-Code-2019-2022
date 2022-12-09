from functools import reduce
with open("input.txt","r") as f: data=f.read().splitlines()
d = [[int(y) for y in x] for x in data]
maxScore = 0
for i in range(len(d)):
    for k in range(len(d[i])):
        score = [0,0,0,0]
        iterators = [reversed(d[i][0:k]), (d[i][k+1:]), reversed([*zip(*d)][k][0:i]), [*zip(*d)][k][i+1:]]
        for m in range(len(score)):
            for j in iterators[m]:
                score[m] += 1
                if j >= d[i][k]:
                    break
        maxScore = max(maxScore,reduce(lambda x, y : x * y, score))
        
print(maxScore)