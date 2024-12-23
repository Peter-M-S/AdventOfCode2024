from collections import defaultdict

# PART1 and 2 by myself, quite slow but acceptable
# filename = "test.txt"
filename = "in.txt"
with open(filename, "r") as f: data = f.readlines()

part1 = part2 = 0
bananas = defaultdict(dict)

for b, secr in enumerate(map(int, data)):
    last_price = secr % 10
    deltas = []
    for i in range(1, 2000 + 1):
        secr = secr ^ (secr * 64)
        secr = secr % 16777216
        secr = secr ^ int(secr / 32)
        secr = secr % 16777216
        secr = secr ^ (secr * 2048)
        secr = secr % 16777216
        price = secr % 10
        deltas.append(price - last_price)
        last_price = price
        if i < 4: continue
        seq = tuple(deltas[i - 4: i])
        if b in bananas[seq]: continue
        bananas[seq][b] = price
    part1 += secr

for seq, bs in bananas.items():
    part2 = max(part2, sum(bs.values()))

print(part1)  # 18694566361
print(part2)  # 2100
