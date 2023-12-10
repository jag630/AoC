import math
data = open("day8.txt").read().split("\n\n")
seq = data[0]
keys = data[1].split("\n")
steps = 0
moves = {}
nodes, cycles = [], []

for move in keys:
    key = move.split(" = ")[0]
    left = move.split(" = ")[1].split(", ")[0].strip("(").strip(")")
    right = move.split(" = ")[1].split(", ")[1].strip("(").strip(")")
    moves[key] = [left, right]
    if key[-1] == "A":
        nodes.append(key)
        cycles.append(0)

while True:
    for x, node in enumerate(nodes):
        nodes[x] = moves[node][0 if seq[steps%len(seq)] == "L" else 1]
        if nodes[x][-1] == "Z": cycles[x] = steps + 1
    steps += 1
    if cycles.count(0) == 0: break
    
print(math.lcm(*cycles))
    
