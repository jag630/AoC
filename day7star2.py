data = open("day7.txt").read().split("\n")
data = [line.split() for line in data]
values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
hands, scores  = {}, {}
winnings, score  = 0, 1
rank = len(data)

for hand, bid in data:
    hands[hand] = int(bid)

cat = {"five" : {},
       "four" : {},
       "full" : {},
       "three" : {},
       "twotwo" : {},
       "two" : {},
       "high" : {}}

for first in values:
    for second in values:
        for third in values:
            for fourth in values:
                for fifth in values:
                    scores [first+second+third+fourth+fifth] = score
                    score += 1

def wintype(hand):
    counts = []
    for i in range(5):
        counts.append(hand.count(hand[i]))
    if counts.count(5) == 5:
        return "five"
    elif counts.count(4) == 4:
        return "five" if hand.count("J") in [1, 4] else "four"
    elif counts.count(3) == 3 and counts.count(2) == 2:
        return "five" if hand.count("J") > 0 else "full"
    elif counts.count(3) == 3:
        return "four" if hand.count("J") > 0 else "three"
    elif counts.count(2) == 4:
        if hand.count("J") == 2:
            return "four"
        elif hand.count("J") == 1:
            return "full"
        return "twotwo"
    elif counts.count(2) == 2:
        return "three" if hand.count("J") > 0 else "two"
    else:
        return "two" if hand.count("J") > 0 else "high"
    
for hand in hands.keys():
    cat[wintype(hand)][hand] = scores[hand]

for key, dic in cat.items():
    for x in range(len(dic)):
        winnings += rank * hands[max(cat[key], key=cat[key].get)]
        cat[key].pop(max(cat[key], key=cat[key].get))
        rank -= 1

print(winnings)
