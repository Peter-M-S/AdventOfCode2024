# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re

part1 = part2 = 0
# data = open(0).read().splitlines()
# with open("test.txt", "r") as f: data = f.read().splitlines()
with open("in.txt", "r") as f: data = f.read().splitlines()

robots = [list(map(int, re.findall(r"-?\d+", line))) for line in data]
# print(robots)

# rows, cols = 7, 11
rows, cols = 103, 101


# PART 1, very slow but correct
time = 100
for i, (c, r, dc, dr) in enumerate(robots):
    nc = (c + dc * time) % cols
    nr = (r + dr * time) % rows
    robots[i][0] = nc
    robots[i][1] = nr

grid = {(r, c): sum([c, r] == rob[:2] for rob in robots) for r in range(rows) for c in range(cols)}

q1 = sum(grid[r, c] for r in range(0, rows // 2) for c in range(0, cols // 2))
q2 = sum(grid[r, c] for r in range(rows // 2 + 1, rows) for c in range(cols // 2 + 1, cols))
q3 = sum(grid[r, c] for r in range(0, rows // 2) for c in range(cols // 2 + 1, cols))
q4 = sum(grid[r, c] for r in range(rows // 2 + 1, rows) for c in range(0, cols // 2))

part1 = q1 * q2 * q3 * q4
print(part1)
