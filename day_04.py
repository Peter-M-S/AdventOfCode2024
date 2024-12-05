# copy data to test.txt and in.txt
# aliases in terminal to run day_00.py:
#   'aot' for test, 'aos' for puzzle input, 'aoc' to run both

part1 = part2 = 0
data = open(0).read()
grid = data.splitlines()
w, h = len(grid[0]), len(grid)
XMAS = {"XMAS", "SAMX"}
for r in range(h):
    for c in range(w):
        if grid[r][c] in "MA": continue
        hor = "".join([grid[r][c + i] for i in range(4) if c < w - 3])
        ver = "".join([grid[r + i][c] for i in range(4) if r < h - 3])
        dia1 = "".join([grid[r + i][c + i] for i in range(4) if r < h - 3 and c < w - 3])
        dia2 = "".join([grid[r + i][c - i] for i in range(4) if r < h - 3 and 2 < c])
        part1 += (hor in XMAS) + (ver in XMAS) + (dia1 in XMAS) + (dia2 in XMAS)
print(part1)

MAS = {"MAS", "SAM"}
for r in range(1, h-1):
    for c in range(1, w-1):
        if grid[r][c] != "A": continue
        dia3 = "".join([grid[r + i][c + i] for i in (-1, 0, 1)])
        dia4 = "".join([grid[r + i][c - i] for i in (-1, 0, 1)])
        part2 += (dia3 in MAS) and (dia4 in MAS)
print(part2)
