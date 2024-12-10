# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both

from time import perf_counter


# now, not afraid of very long list, modify the disk directly
# use (start, length) tuples for part2


def shift_block(D: list) -> list:
    n = len(D)
    j = n - 1
    f = D.count(".")
    for i in range(n - f):
        if D[i] != ".": continue
        while D[j] == ".": j -= 1
        D[i], D[j] = D[j], D[i]
    return D


def shift_file(F: dict, S: list) -> dict:
    for f_id, (f_start, f_len) in reversed(F.items()):
        for i, (s_start, s_len) in enumerate(S):
            if f_start < s_start: break  # no more spaces left of file
            if f_len > s_len: continue  # file too big for this space

            F[f_id] = (s_start, f_len)
            s_len -= f_len
            if s_len:
                S[i] = (s_start + f_len, s_len)
            else:
                S.pop(i)
            break  # must exit the loop, because S was modified
    return F


def checksum(D: list):
    return sum(i * n for i, n in enumerate(D) if n != ".")


#

def split_disk(data):
    F = {}  # k: file-id, v: (start-index, length)
    S = []  # [lengths of free spaces on disk]
    ID = 0  # file-id
    IDX = 0  # disk-index
    i = 0  # data-index of input string
    while True:
        b = int(data[i])
        F[ID] = (IDX, b)
        IDX += b
        ID += 1
        i += 1

        if i >= len(data): break

        f = int(data[i])
        if f != 0:
            S.append((IDX, f))
            IDX += f
        i += 1

    return F, S


def get_disk(files) -> list:
    D = []
    # loop files in order of f_start
    for f_id, (f_start, f_len) in sorted(files.items(), key=lambda id__s_l: id__s_l[1][0]):
        while len(D) < f_start:
            D += ["."]
        D += [f_id] * f_len
    return D


part1 = part2 = 0

time0 = perf_counter()
# data = open(0).readline()
# with open("test.txt", "r") as f: data = f.readline()
with open("in.txt", "r") as f: data = f.readline()

D = []  # list of blocks on disk
file_id = 0
space_id = "."

for i, c in enumerate(data):
    if i % 2:
        D += [space_id] * int(c)
    else:
        D += [file_id] * int(c)
        file_id += 1

D2 = D.copy()  # keep unmodified for part2

# for part1 shift blocks
D = shift_block(D)
print("checksum...")
part1 = checksum(D)
print(part1)  # 6448989155953
print(f"part1 time {perf_counter() - time0}")
time1 = perf_counter()
print()

# for part2 shift files
files, spaces = split_disk(data)
files = shift_file(files, spaces)
D = get_disk(files)
print("checksum...")
part2 = checksum(D)
print(part2)  # 6476642796832
print(f"part2 time {perf_counter() - time1}")
