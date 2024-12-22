# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict

DIRECTIONS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS8 = ((dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0))


def on_grid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def floodfill(a: set, r: int, c: int, t: str) -> set:
    for dr, dc in DIRECTIONS4:
        if not on_grid(r + dr, c + dc, rows, cols): continue
        if grid[r + dr][c + dc] != t: continue
        if (r + dr, c + dc) in a: continue
        a |= floodfill(a | {(r + dr, c + dc)}, r + dr, c + dc, t)
    return a


part1 = part2 = 0
# grid = open(0).read().splitlines()
# with open("test.txt", "r") as f: grid = f.read().splitlines()
with open("in.txt", "r") as f: grid = f.read().splitlines()
cols, rows = len(grid[0]), len(grid)

regions = defaultdict(list)  # need calculate to separate regions of same type
seen = set()
borders = defaultdict(list)
corners = defaultdict(int)


def border_map(r, c) -> list[bool]:
    # u, r, d, l: true when there is a border
    return [not on_grid(r+dr, c+dc, rows, cols) or grid[r+dr][c+dc] != grid[r][c] for dr, dc in DIRECTIONS4]


def is_enclave(t2: str, j: int, inner: set, outer: set) -> bool:

    # number of pos of inner that have border to outer == outer_edges[inner]
    n = 0
    for r, c in inner:
        u, right, d, l = borders[(r,c)]
        if u: n += (r-1, c) in outer
        if right: n += (r, c+1) in outer
        if d: n += (r+1, c) in outer
        if l: n += (r, c-1) in outer

    return perimeters[t2][j] == n


for r, row in enumerate(grid):
    for c, t in enumerate(row):
        if (r, c) not in seen:
            flooded: set = floodfill({(r, c)}, r, c, t)
            seen |= flooded
            regions[t].append(flooded)
        borders[(r, c)] = border_map(r, c)
perimeters = defaultdict(list)
for t, regs in regions.items():
    t_sum = 0
    for reg in regs:
        perimeter = 0
        for pos in reg:
            perimeter += sum(borders[pos])
        perimeters[t].append(perimeter)
        t_sum += perimeter * len(reg)
    part1 += t_sum
print(part1)        # 1485656
print(perimeters)
# 1. follow outer perimeter of each region keep count of turns to calculate straight edges
# 2. check if any "islands" inside a region, and add straight edges of that outer perimeter

outer_edges = defaultdict(list)
for t, regs in regions.items():
    for reg in regs:
        start, edges = min(reg), 0
        r, c = start
        dr, dc = 0, 1   # initial walking direction to right
        b, no_b = 0, 1   # initial position has border at top, no right border
        assert borders[start][3]    # inital position has left border
        while not (edges >= 4 and (r, c) == start and (dr, dc) == (0, 1)):
            while borders[(r, c)][b] and not borders[(r, c)][no_b]:
                r, c = r+dr, c+dc

            if borders[(r, c)][b] and borders[(r, c)][no_b]:  # -> turn CW
                dr, dc = dc, -dr
                edges += 1
                b += 1
                if b == 4: b = 0
                no_b += 1
                if no_b == 4: no_b = 0
                continue

            if not borders[(r, c)][b]:  # -> turn CCW
                dr, dc = -dc, dr
                r, c = r+dr, c+dc
                edges += 1
                b -= 1
                if b == -1: b = 3
                no_b -= 1
                if no_b == -1: no_b = 3
                continue

        outer_edges[t].append(edges)

print(outer_edges)

enclaves = defaultdict(list)
for t, regs in regions.items():
    for i, reg in enumerate(regs):
        for t2, regs2 in regions.items():
            if t == t2: continue
            for i2, reg2 in enumerate(regs2):
                if is_enclave(t2, i2, reg2, reg):
                    enclaves[t].append((i, t2, i2))
print(enclaves)

for t, regs in regions.items():
    for i, reg in enumerate(regs):
        edges = outer_edges[t][i]
        for i2, t2, j in enclaves[t]:
            if i2 != i: continue
            edges += outer_edges[t2][j]
        print(t, edges)
        part2 += len(reg) * edges

print(part2)    # 911384 too high
