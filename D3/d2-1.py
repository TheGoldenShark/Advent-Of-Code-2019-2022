with open("input.txt","r") as f: data=f.read().splitlines()

prior = lambda x : ord(x) - 96 if ord(x) > 96 else ord(x) - 38

d = [list(x) for x in data]
duplicates = []
for x in d:
    x1 = x[:int(len(x)/2)]
    x2 = x[int(len(x)/2):]
    duplicates.append(set(x1).intersection(set(x2)).pop())

print(sum([prior(x) for x in duplicates]))


