data = open("day5.txt").read().split("\n\n")
seeds = [int(x) for x in data[0].split()[1:]]
maps = []
location = 0

for x in range(1, len(data)):
    maps.append(data[x].split("\n")[1:])

for x, amap in enumerate(maps):
    for y, line in enumerate (amap):
        line = line.split()
        maps[x][y] = [int(z) for z in line]

for seed in seeds:
    for amap in maps:
        for dest, source, rang in amap:
            if source <= seed <= source + rang - 1:
                seed = dest + seed - source
                break
    else:
        if location == 0: location = seed
        else: location = min(location, seed)

print(location)
