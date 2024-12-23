from collections import deque

# filename, max_i, steps = "test.txt", 6, 12
filename, max_i, steps = "in.txt", 70, 1024
with open(filename, "r") as f: data = f.readlines()  # data = c,r

part1 = 0

corrupted = {tuple(map(int, line.split(",")[::-1])) for line in data[:steps]}  # (r, c)

target = (max_i, max_i)
q = deque([((0, 0), 0)])

seen = set()
while q:
    (r, c), path = q.popleft()
    if (r, c) == target:
        part1 = path
        break
    for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
        if not (0 <= nr <= max_i and 0 <= nc <= max_i): continue
        if (nr, nc) in corrupted | seen: continue
        seen.add((nr, nc))
        q.append(((nr, nc), path + 1))

print(part1)  # 260
