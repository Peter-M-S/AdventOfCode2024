# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict
from functools import cache
# works for both parts but too slow (>1h)


@cache
def cheat(sr0, sc0, i0, r, c, s):
    if s == cheat_time: return
    if not (0 < r < rows - 1, 0 < c < cols - 1): return
    ns = s + 1
    for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
        i = path.index((nr, nc)) if (nr, nc) in path_set else -1
        cut = i - i0 - ns
        if cut >= cut_min:
            # print(f"found cut from {sr0, sc0} to {nr, nc} with {ns:2d} steps to save {cut}")
            candidates[cut].add(((sr0, sc0), (nr, nc)))
        cheat(sr0, sc0, i0, nr, nc, ns)


part1 = part2 = 0
# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()
grid = data.splitlines()
path_set = set()
SR = SC = ER = EC = 0
for r, row in enumerate(grid):
    for c, s in enumerate(row):
        if s == "#": continue
        if s == "S": SR, SC = r, c
        if s == "E": ER, EC = r, c
        path_set.add((r, c))
rows, cols = r + 1, c + 1
PATHLENGTH = len(path_set)
r, c = SR, SC
path = [(SR, SC)]
while len(path) < PATHLENGTH:
    for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
        if (nr, nc) not in path_set: continue
        if (nr, nc) in path: continue
        path.append((nr, nc))
        break
    r, c = nr, nc

cheat_time = 20
cut_min = 100  # minimum saving time
candidates = defaultdict(set)
for i, (r, c) in enumerate(path):
    print(i, PATHLENGTH)
    cheat(r, c, i, r, c, 0)

cuts = list(candidates)
for cut in cuts[::-1]:
    for n in range(cut - 1, cut_min - 1, -1):       # keep a position only in the highest cut
        if n not in candidates: continue
        candidates[n].difference_update(candidates[cut])

part2 = sum(len(c) for c in candidates.values())
print(part2)
