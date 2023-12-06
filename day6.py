data = open("day6.txt").read().split("\n")
times = list(map(int, data[0].split(":")[1].split()))
dists = list(map(int, data[1].split(":")[1].split()))
bigtime = int("".join(data[0].split(":")[1].split()))
bigdist = int("".join(data[1].split(":")[1].split()))
prod = 1

def wins(time, dist):
    for held in range(time):
        if (time - held) * held > dist:
            mintime = held
            break
    for held in range(time, -1, -1):
        if (time - held) * held > dist:
            maxtime = held
            break
    return maxtime - mintime + 1
    
for x, time in enumerate(times):
    prod *= wins(time, dists[x])
   
print(prod)
print(wins(bigtime, bigdist))
