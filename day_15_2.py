# AOC 2024 Day 15 Part 2


def show_grid(grid, rows, cols):  # heavily needed for debugging
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


def move_box(grid, boxes, box, dr, dc):
    r, c = box
    cL, cR = c - 0.5, c + 0.5
    grid[r, cL], grid[r, cR] = ".."
    del boxes[box]

    boxes[r + dr, c + dc] = {(r + dr, cL + dc), (r + dr, cR + dc)}
    grid[r + dr, cL + dc], grid[r + dr, cR + dc] = "[]"

    return grid, boxes


def move_pack(grid, boxes, pack, dr, dc) -> tuple[dict, tuple]:
    for box in pack[::-1]:
        grid, boxes = move_box(grid, boxes, box, dr, dc)
    return grid, boxes


def get_pack(walls, boxes, bot, dr, dc) -> list:
    # return list of boxes that can be moved together, empty list if blocked
    pack, nr, nc = [], bot[0] + dr, bot[1] + dc
    # move left/right
    if dr == 0 and dc != 0:
        while (nr, nc + 0.5 * dc) in boxes:
            pack.append((nr, nc + 0.5 * dc))
            nc += 2 * dc
            if (nr, nc) in walls: return []
        return pack
    # move up/down
    front: list = [(nr, nc)]
    boxes2pack = {(r, c) for r, c in boxes if (r, c + 0.5) in front or (r, c - 0.5) in front}
    while boxes2pack:
        pack += list(boxes2pack)
        front = []
        for r, c in boxes2pack:
            front.append((r + dr, c - 0.5))
            front.append((r + dr, c + 0.5))
        if any((r, c) in walls for r, c in front): return []
        boxes2pack = {(r, c) for r, c in boxes if (r, c + 0.5) in front or (r, c - 0.5) in front}
    return pack


part1 = part2 = 0
# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

data, instructions = data.split("\n\n")
directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
instructions = [directions[s] for s in instructions if s != "\n"]
boxes = dict()
walls = set()
bot = (0, 0)
data = data.splitlines()

ddata = []
for line in data:
    double: str = ""
    for s in line:
        if s == "#": double += "##"
        if s == "O": double += "[]"
        if s == ".": double += ".."
        if s == "@": double += "@."
    ddata.append(double)
rows, cols = len(ddata), len(ddata[0])

grid = {(r, c): s for r, row in enumerate(ddata) for c, s in enumerate(row)}
for r in range(rows):
    for c in range(cols):
        if grid[r, c] in ".": continue
        if grid[r, c] == "#": walls.add((r, c))
        if grid[r, c] == "[":
            boxes[r, c + 0.5] = {(r, c), (r, c + 1)}  # box has column coordinates at .5
        if grid[r, c] == "@": bot = (r, c)

# show_grid(grid, rows, cols)
for i, (dr, dc) in enumerate(instructions):
    nr, nc = bot[0] + dr, bot[1] + dc
    if (nr, nc) in walls: continue

    if (nr, nc - 0.5) not in boxes and (nr, nc + 0.5) not in boxes:
        grid, bot = move_bot(grid, bot, dr, dc)
        continue

    pack = get_pack(walls, boxes, bot, dr, dc)
    if not pack: continue
    grid, boxes = move_pack(grid, boxes, pack, dr, dc)
    grid, bot = move_bot(grid, bot, dr, dc)

# show_grid(grid, rows, cols)
part2 = sum(r * 100 + int(c) for r, c in boxes)

print(part2)
