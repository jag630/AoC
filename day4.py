data = open("day4.txt").read().split("\n")
cardscore, winnum, thesum = 0, 0, 0
cardcounts = []

for i in range(len(data)):
    cardcounts.append(1)
               
for x, row in enumerate(data):
    wins = row.split("|")[0].split(":")[1].split()
    nums = row.split("|")[1].split()
    for num in nums:
        if num in wins:
            winnum += 1
            if cardscore == 0: cardscore = 1
            else: cardscore *= 2
    for i in range(winnum):
        cardcounts[x + i + 1] += cardcounts[x]
    thesum += cardscore
    cardscore, winnum = 0, 0

print(thesum)
print(sum(cardcounts))

