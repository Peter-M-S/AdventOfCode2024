# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both

def move(g: tuple) -> tuple:
    r, c, h = g
    next_pos = (r + h.real, c + h.imag)
    if next_pos in obstacles:
        h = h * (-1j)   # turn right ( CW )
    else:
        r, c = next_pos
    return r, c, h


part1 = part2 = 0
data = open(0).read().splitlines()
w, h = len(data[0]), len(data)
grid = {(r, c): data[r][c] for c in range(w) for r in range(h)}
head: complex = (-1 + 0j)       # row, col - init up
seen = set()
obstacles = set()
guard0 = (h, w, head)           # r, c, head - init off grid
for r in range(h):
    for c in range(w):
        if grid[(r, c)] == "#": obstacles.add((r, c))
        elif grid[(r, c)] == "^": guard0 = (r, c, head)

guard = guard0
visited = set()
while tuple(guard[:2]) in grid:
    seen.add(guard)
    visited.add(tuple(guard[:2]))     # head doesn't matter for part1
    guard = move(guard)
part1 = len(visited)

path_grid = {k: v for k, v in grid.items() if k in visited and k != tuple(guard0[:2])}
# after this added it is a bit faster

for pos in path_grid:   # obstacles and guard0 excluded already in path_grid
    obstacles.add(pos)
    guard = guard0
    seen = {guard}
    while tuple(guard[:2]) in grid:
        seen.add(guard)     # need pos + head
        guard = move(guard)
        if guard in seen:   # found loop
            part2 += 1
            break
    obstacles.remove(pos)

print(part1)
print(part2)
