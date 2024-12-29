from collections import defaultdict

DIRECTIONS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def on_grid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def floodfill(a: set, r: int, c: int, t: str) -> set:
    for dr, dc in DIRECTIONS4:
        if not on_grid(r + dr, c + dc, rows, cols) or grid[r + dr][c + dc] != t or (r + dr, c + dc) in a:
            continue
        a |= floodfill(a | {(r + dr, c + dc)}, r + dr, c + dc, t)
    return a


def border_map(r, c) -> list[bool]:  # u, r, d, l: true when there is a border
    return [not on_grid(r + dr, c + dc, rows, cols) or grid[r + dr][c + dc] != grid[r][c] for dr, dc in DIRECTIONS4]


part1 = part2 = 0

# with open("test.txt", "r") as f: grid = f.read().splitlines()
with open("in.txt", "r") as f: grid = f.read().splitlines()
cols, rows = len(grid[0]), len(grid)

regions = defaultdict(list)  # need calculate to separate regions of same type
seen = set()
borders = dict()

for r, row in enumerate(grid):
    for c, t in enumerate(row):
        if (r, c) not in seen:
            flooded: set = floodfill({(r, c)}, r, c, t)
            seen |= flooded
            regions[t].append(flooded)
        borders[r, c] = border_map(r, c)

for t, regs in regions.items():
    for reg in regs:
        perimeter = sum(sum(borders[pos]) for pos in reg)
        part1 += perimeter * len(reg)

print(f"{part1=}")  # 1485656

# count all corners of a region (= number of straight lines)
corner_map = defaultdict(set)
for t, regs in regions.items():
    for reg in regs:
        for r, c in reg:
            corner_pos = {(r - 0.5, c - 0.5), (r - 0.5, c + 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5)}
            corner_map[t] |= corner_pos

for t, regs in regions.items():
    for reg in regs:
        corners = 0
        for r5, c5 in corner_map[t]:
            corner_type = []
            for r, c in ((r5 - .5, c5 - .5), (r5 - .5, c5 + .5), (r5 + .5, c5 + .5), (r5 + .5, c5 - .5)):
                corner_type.append((r, c) in reg)   # top-left, top-right, bottom-right, bottom-left
            corners += sum(corner_type) in (1, 3)   # 1 outer or 1 inner corner
            corners += 2 * (corner_type in [[False, True, False, True], [True, False, True, False]])  # 2 outer corners
        part2 += corners * len(reg)

print(f"{part2=}")  # 899196
