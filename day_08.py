# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict
import itertools


def find_antinodes(p, q, rows, cols, part2):
    (pr, pc), (qr, qc) = p, q
    dr, dc = pr - qr, pc - qc
    result = set()
    r, c = pr + dr, pc + dc
    while on_grid(r, c, rows, cols):
        result.add((r, c))
        if not part2: return result
        r += dr
        c += dc
    if part2: result.add(p)
    return result


def on_grid(r, c, rows, cols): return 0 <= r < rows and 0 <= c < cols


part1 = part2 = 0
grid = open(0).read().splitlines()
# with open("test.txt", "r") as f: grid = f.read().splitlines()
# with open("in.txt", "r") as f: data = f.read().splitlines(

cols, rows = len(grid[0]), len(grid)
nodes = defaultdict(set)
antinodes = set()

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".": nodes[grid[r][c]].add((r, c))

for node in nodes.values():
    for p, q in itertools.permutations(node, 2):
        for r, c in find_antinodes(p, q, rows, cols, False):
            antinodes.add((r, c))
part1 = len(antinodes)

for node in nodes.values():
    for p, q in itertools.permutations(node, 2):
        for r, c in find_antinodes(p, q, rows, cols, True):
            antinodes.add((r, c))
part2 = len(antinodes)

print(part1)  # 348
print(part2)  # 1221
