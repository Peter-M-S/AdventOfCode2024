# filename = "test.txt"
filename = "in.txt"
with open(filename, "r") as f: data = f.read()

part1 = part2 = 0

blocks = data.split("\n\n")
locks, keys = set(), set()

for block in blocks:
    block = block.splitlines()
    a = tuple(line.count("#") for line in zip(*block[1:-1]))
    keys.add(a) if "#" in block[0] else locks.add(a)

for key in keys:
    part1 += sum(all(sum(p) <= 5 for p in zip(key, lock)) for lock in locks)

print(part1)
