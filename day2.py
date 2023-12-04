gamesum, powersum = 0, 0

for game in open("day2.txt").read().split("\n"):
    gamenum, draws = game.split(":")
    counts = {}
    for draw in draws.split(";"):
        for cube in draw.split(","):
            num, color = cube.split()
            counts[color] = max(counts.get(color, 0), int(num))
    if counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14:
        gamesum += int(gamenum.split()[1])
    powersum += counts["red"] * counts["green"] * counts["blue"]

print(gamesum)
print(powersum)
