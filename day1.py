def calc(words):
    thesum = 0
    spell = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    vals = {}
    for i in range(1, 10):
        if words: vals[spell[i]] = i
        vals[str(i)] = i
        
    for line in open("day1.txt").read().split("\n"):
        hits = []
        for x in range(len(line)):
            for string in vals:
                if line[x:].startswith(string):
                    hits.append(vals[string])
        thesum += hits[0]*10 + hits[-1]
    return thesum
    
print(calc(False))
print(calc(True))

