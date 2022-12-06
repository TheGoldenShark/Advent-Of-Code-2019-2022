with open("input.txt","r") as f: data=f.read().splitlines()
d = [x for x in data[0]]
queue = [d[x] for x in range(4)]
if len(set(queue)) == 4:
    print(1)
else: 
    for i in range(4, len(d)):
        queue.pop(0)
        queue.append(d[i])
        if len(set(queue)) == 4:
            print(i+1)
            break

