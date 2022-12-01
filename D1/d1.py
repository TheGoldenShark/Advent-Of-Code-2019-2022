# HAPPY CRIMMAS
with open("input.txt","r") as f: data=f.readlines()
d = [-1 if x == '\n' else int(x[:-1]) for x in data] 
elves = []
calories = 0
for i in d:
    if i == -1:
        elves.append(calories)
        calories = 0
    else:
        calories += i

print(max(elves))