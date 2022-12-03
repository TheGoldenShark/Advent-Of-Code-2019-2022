with open("input.txt","r") as f: data=f.read().splitlines()
d = [list(x) for x in data]
prior = lambda x : ord(x) - 96 if ord(x) > 96 else ord(x) - 38
badges = []
for x in range(int(len(d)/3)):
    badges.append(set.intersection(set(d[3*x]),set(d[3*x + 1]), set(d[3*x + 2])).pop())

print(sum([prior(x) for x in badges]))



