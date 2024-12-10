# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict

part1 = part2 = 0

data = open(0).read().splitlines()
# with open("test.txt", "r") as f: data = f.read().splitlines()
# with open("in.txt", "r") as f: grid = f.read().splitlines()

cols, rows = len(data[0]), len(data)
grid = {(r, c): int(data[r][c]) for c in range(cols) for r in range(rows)}

summits = defaultdict(list)
for h in (9, 8, 7, 6, 5, 4, 3, 2, 1, 0):
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != h: continue
            if h == 9:
                summits[r, c] = [(r, c)]
                continue
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if grid.get((r + dr, c + dc), -1) == h + 1:
                    summits[r, c].extend(summits[r + dr, c + dc])

part1 = sum(len(set(v)) for k, v in summits.items() if grid[k] == 0)
part2 = sum(len(v) for k, v in summits.items() if grid[k] == 0)

print(part1)
print(part2)
