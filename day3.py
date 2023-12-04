data = open("day3.txt").read().split("\n")
num = ""
thesum, gearsum = 0, 0
prevDig, bySymbol, byAst = False, False, False
asts = {}

data.insert(0, "."*len(data[0])+"..")
for x, row in enumerate(data): data[x] = "."+row+"."
data.append("."*len(data[0])+"..")

for x, row in enumerate(data):
    for y, ch in enumerate(row):
        if ch.isdigit():
            num += ch
            prevDig = True
            for i, j in [(i, j) for i in range(-1, 2) for j in range(-1, 2)]:
                adj = data[x+i][y+j]
                if not adj.isdigit() and adj != ".":
                    bySymbol = True
                if adj == "*":
                    byAst = True
                    astPoint = (x+i, y+j)
                    asts[astPoint] = asts.get(astPoint, [])
        elif prevDig:
            if bySymbol: thesum += int(num)
            if byAst: asts[astPoint].append(int(num))
            byAst, prevDig, bySymbol = False, False, False
            num = ""

for val in asts.values():
    if len(val) == 2: gearsum += val[0] * val[1]
        
print(thesum)
print(gearsum)
