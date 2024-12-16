# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict
from heapq import heappush, heappop

part1 = part2 = 0
# data = open(0).readlines()
with open("test.txt", "r") as f: data = f.readlines()
# with open("in.txt", "r") as f: data = f.readlines()
START = FIN = (0,0)
grid = [line.strip() for line in data]
for r, line in enumerate(grid):
    if "E" in line: FIN = (r, line.index("E"))
    if "S" in line: START = (r, line.index("S"))

q = []
heappush(q, (0, *START, 0, 1))
costs = defaultdict()
costs[(*START, 0, 1)] = 0
while q:
    crc, r, c, dr, dc = heappop(q)
    # find next moves (follow dr, dc, turn CW, turn CCW)
    for cost, (nr, nc, ndr, ndc) in zip((1, 1000, 1000), ((r+dr, c+dc, dr, dc), (r, c, dc, -dr), (r, c, -dc, dr))):
        if grid[nr][nc] == "#": continue
        if (nr, nc) == FIN:
            print("FIN")
            part1 = crc+cost
            q = []
            break
        if costs.get((nr, nc, ndr, ndc), float("inf")) > crc+cost:
            heappush(q, (crc+cost, nr, nc, ndr, ndc))
            costs[(nr,nc,dr,dc)] = crc+cost

print(part1)
