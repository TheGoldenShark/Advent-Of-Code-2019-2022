with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [[y if y[0] == 'a' or y[0] == 'n' else int(y) for y in x.split(" ")] for x in data]
regX = 1
cycle = 1
wait = False
add = 0
signal = 0
for i in d:
    if wait:
        cycle += 1
        wait = False
        regX += add
        if ((cycle) >= 20 and (((cycle) - 20) % 40) == 0):
            signal+= regX * cycle
    if i[0] == "noop":
        cycle += 1
    elif i[0] == "addx":
        add = i[1]
        wait = True
        cycle += 1
    if ((cycle) >= 20 and (((cycle) - 20) % 40) == 0):
        signal+= regX * cycle
print(signal)
