with open("input.txt","r") as f: data=f.read().splitlines()
d = [x for x in data[0]]
queue = [d[x] for x in range(14)]
if len(set(queue)) == 14:
    print(1)
else: 
    for i in range(14, len(d)):
        queue.pop(0)
        queue.append(d[i])
        if len(set(queue)) == 14:
            print(i+1)
            break

