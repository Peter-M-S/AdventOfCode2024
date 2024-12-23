from collections import deque

# filename, max_i, steps = "test.txt", 6, 12
filename, max_i, steps = "in.txt", 70, 1024
with open(filename, "r") as f: data = f.readlines()  # data = c,r


def corrupted(steps):
    return {tuple(map(int, line.split(",")[::-1])) for line in data[:steps]}  # (r, c)


def has_path(corrupted):
    q = deque([(0, 0)])
    seen = set()
    while q:
        (r, c) = q.popleft()
        if (r, c) == target: return True
        for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
            if not (0 <= nr <= max_i and 0 <= nc <= max_i): continue
            if (nr, nc) in corrupted | seen: continue
            seen.add((nr, nc))
            q.append((nr, nc))
    return False


target = (max_i, max_i)
low = steps - 1
high = len(data)
mid = float("inf")
while low < high:
    mid = ((low + high) // 2)
    corr = corrupted(mid)  # all fallen before mid
    if has_path(corr):  # blocker is in mid+1:high
        low = mid + 1
    else:  # blocker is in low:mid
        high = mid

part2 = data[mid - 1].strip()

print(part2)  # 24,48
