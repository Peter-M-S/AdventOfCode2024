# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict

part1 = part2 = 0
# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

grid = data.splitlines()
path_set = set()
for r, row in enumerate(grid):
    for c, s in enumerate(row):
        if s == "#": continue
        if s == "S": sr, sc = r, c
        if s == "E": er, ec = r, c
        path_set.add((r, c))
rows, cols = r + 1, c + 1
PATHLENGTH = len(path_set)
r, c, i = sr, sc, 0
path = {(r, c): i}
while len(path) < PATHLENGTH:
    for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
        if (nr, nc) not in path_set: continue
        if (nr, nc) in path: continue
        i += 1
        path[nr, nc] = i
        break
    r, c = nr, nc

cut_min = 100  # minimum saving time
# PART 1
candidates = defaultdict(set)
for (r, c), i in path.items():
    for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
        if (nr, nc) in path: continue
        for nnr, nnc in ((nr - 1, nc), (nr, nc + 1), (nr + 1, nc), (nr, nc - 1)):
            if (nnr, nnc) not in path: continue
            cut = path[nnr, nnc] - i - 2
            if cut >= cut_min:
                candidates[cut].add(((r, c), (nnr, nnc)))

part1 = sum(len(c) for c in candidates.values())
print(part1)
