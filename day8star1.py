data = open("day8.txt").read().split("\n\n")
seq = data[0]
keys = data[1].split("\n")
moves = {}
steps = 0
current = "AAA"

for move in keys:
    key = move.split(" = ")[0]
    left = move.split(" = ")[1].split(", ")[0].strip("(").strip(")")
    right = move.split(" = ")[1].split(", ")[1].strip("(").strip(")")
    moves[key] = [left, right]

while current != "ZZZ":
    current = moves[current][0 if seq[steps%len(seq)] == "L" else 1]
    steps += 1
    
print(steps)
    
    
