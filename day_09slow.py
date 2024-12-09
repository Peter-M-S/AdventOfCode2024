# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict
from copy import deepcopy
from time import perf_counter


# 7 minutes to calculate both solutions :-(
# very slow, but successful


def shift_block(id, B, F) -> tuple:
    if min(F) > max(B[id]): return False, B, F
    fidx, F = F[0], F[1:]
    bidx = B[id].pop()
    B[id] = [fidx] + B[id]
    B[id].sort()
    F.append(bidx)
    F.sort()
    return True, B, F


def shift_file(id, B, F) -> tuple:
    stretches = get_free_stretches(F)
    start = 0
    b: list = B[id]
    for i, stretch in enumerate(stretches):
        if min(stretch) > max(b): continue
        if len(stretch) >= len(b):
            B[id] = [F[start + j] for j in range(len(b))]
            for j, n in enumerate(b):
                F[start + j] = n
            F.sort()
            return True, B, F
        start += len(stretch)
    return False, B, F


def show_disk(B, F, disk_space):    # for debugging the examples
    for i in range(disk_space):
        s = "X"
        if i in F:
            s = "."
        else:
            for k, v in B.items():
                if i in v:
                    s = str(k)
        print(s, end="")
    print()


def checksum(B, F, disk_space):
    n = 0
    for i in range(disk_space):
        if i in F: continue
        for k, v in B.items():
            if i in v:
                n += i * k
                break
    return n


def get_free_stretches(F):
    stretches = []
    stretch = [F[0]]
    for n in F[1:]:
        if n - 1 == stretch[-1]:
            stretch.append(n)
        else:
            stretches.append(stretch)
            stretch = [n]
    stretches.append(stretch)
    return stretches


part1 = part2 = 0

time0 = perf_counter()
data = open(0).readline()
# with open("test.txt", "r") as f: data = f.readline()
# with open("in.txt", "r") as f: data = f.read().splitlines()

data_n = len(data)
B = defaultdict(list)  # k: block-id, v: [IDX of id on disk]
F = []  # [IDX of free on disk]
ID = 0
IDX = 0
i = 0  # index of input string
for _ in range(data_n):
    b = int(data[i])
    B[ID] = list(n for n in range(IDX, IDX + b))
    IDX += b
    ID += 1
    i += 1

    if i >= data_n: break

    f = int(data[i])
    F.extend(n for n in range(IDX, IDX + f))
    IDX += f
    i += 1

ids = list(B.keys())[::-1]

disk_space = max(max(F), max([max(b) for b in B.values()])) + 1

B2 = deepcopy(B)
F2 = deepcopy(F)

for id in ids:
    if not id % 10: print(id)
    can_move = True
    while can_move:
        can_move, B, F = shift_block(id, B, F)

print("start checksum1")
part1 = checksum(B, F, disk_space)

for id in ids:
    if not id % 10: print(id)
    can_move = True
    while can_move:
        can_move, B2, F2 = shift_file(id, B2, F2)

print("start checksum2")
part2 = checksum(B2, F2, disk_space)

print(f"time {perf_counter() - time0}")
print(part1)  # 6448989155953
print(part2)  # 6476642796832
