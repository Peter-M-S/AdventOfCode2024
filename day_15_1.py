# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both


def show_grid(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(grid[(r, c)] or ".", end="")
        print(end="\n")
    print()


def move_bot(grid: dict, bot: tuple, dr: int, dc: int) -> tuple[dict, tuple]:
    grid[bot] = "."
    r, c = bot
    bot = (r + dr, c + dc)
    grid[bot] = "@"
    return grid, bot


def move_pack(grid, boxes, pack, dr, dc) -> tuple[dict, tuple]:
    boxes.remove(pack[0])
    r, c = pack[-1]
    boxes.add((r + dr, c + dc))
    grid[r + dr, c + dc] = "O"
    return grid, boxes


part1 = part2 = 0
# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()
data, instructions = data.split("\n\n")
data = data.splitlines()
rows, cols = len(data), len(data[0])
grid = {(r, c): s for r, row in enumerate(data) for c, s in enumerate(row)}
directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
instructions = [directions[s] for s in instructions if s != "\n"]
boxes = set()
walls = set()
for r in range(rows):
    for c in range(cols):
        if grid[r, c] in ".": continue
        if grid[r, c] == "#": walls.add((r, c))
        if grid[r, c] == "O": boxes.add((r, c))
        if grid[r, c] == "@": bot = (r, c)

for dr, dc in instructions:

    nr, nc = bot[0] + dr, bot[1] + dc
    if (nr, nc) in walls: continue
    if (nr, nc) not in boxes:
        grid, bot = move_bot(grid, bot, dr, dc)
        continue

    pack = []
    while (nr, nc) in boxes:
        pack.append((nr, nc))
        nr += dr
        nc += dc
    if (nr, nc) in walls: continue
    grid, bot = move_bot(grid, bot, dr, dc)
    grid, boxes = move_pack(grid, boxes, pack, dr, dc)
    # show_grid(grid, rows, cols)

part1 = sum(r * 100 + c for r, c in boxes)

print(part1)
