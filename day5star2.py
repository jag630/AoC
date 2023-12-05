data = open("day5.txt").read().split("\n\n")
seeds = [int(x) for x in data[0].split()[1:]]
seedpairs = []

for x in range(0, len(seeds), 2):
    seedpairs.append([seeds[x], seeds[x+1]])

maps = []
for x in range(1, len(data)):
    maps.append(data[x].split("\n")[1:])
for x, amap in enumerate(maps):
    for y, line in enumerate(amap):
        line = line.split()
        maps[x][y] = [int(z) for z in line]

for x in range(0, 100000000000):
    prevnum = x
    for i in range(len(maps)-1, -1, -1):
        for dest, source, rang in maps[i]:
            if dest <= prevnum <= dest + rang - 1:
                prevnum = source + prevnum - dest
                break
    for i, j in seedpairs:
        if prevnum in range(i, i+j):
            print(x)
            break
    else:
        continue
    break
        

