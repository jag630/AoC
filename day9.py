data = open("day9.txt").read().split("\n")
data = [list(map(int, line.split())) for line in data]
endsum, prevsum = 0, 0

for line in data:
    layers = [line]
    layer, temp = 0, 0
    newleft, lineend = line[0], line[-1]
    while True:
        layers.append([])
        for x in range(len(layers[layer])-1):
            layers[layer+1].append(layers[layer][x+1]-layers[layer][x])
        layer += 1
        if layers[-1].count(0) == len(layers[-1]):
            for x in range(layer):
                lineend += layers[x+1][-1]
                newleft = layers[-2-x][0] - temp
                temp = newleft
            endsum += lineend
            prevsum += newleft
            break
                                    
print(endsum, prevsum)
        
    
