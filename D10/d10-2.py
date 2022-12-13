with open("input.txt","r") as f: data=f.read().splitlines()
# with open("input2.txt","r") as f: data=f.read().splitlines()
d = [[y if y[0] == 'a' or y[0] == 'n' else int(y) for y in x.split(" ")] for x in data]
regX = 1
cycle = 1
wait = False
add = 0
signal = 0
crt = [['.' for x in range(40)] for y in range(6)]
for i in d:
    if wait:
        cycle += 1
        wait = False
        if ((cycle-2) % 40 >= regX - 1 and (cycle-2) % 40 <= regX + 1) and (cycle - 1) < (6 * 40):
            crt[int((cycle-2)/40)][(cycle-2) % 40] = "#"
        regX += add
    if i[0] == "noop":
        cycle += 1
    elif i[0] == "addx":
        add = i[1]
        wait = True
        cycle += 1
    if ((cycle-2) % 40 >= regX - 1 and (cycle-2) % 40 <= regX + 1) and (cycle - 1) < (6 * 40):
        crt[int((cycle-2)/40)][(cycle-2) % 40] = "#"
    

for i in crt:
    print(('').join(i))