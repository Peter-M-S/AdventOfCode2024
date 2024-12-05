# copy data to test.txt and in.txt
# aliases in terminal to run day_00.py:
#   'aot' for test, 'aos' for puzzle input, 'aoc' to run both

def is_safe(ls: list) -> bool:
    up: bool = ls[1] > ls[0]
    s = True
    for a, b in zip(ls[:-1], ls[1:]):
        if a == b:
            s = False
            break
        if (b > a) != up:
            s = False
            break
        if abs(b - a) not in (1, 2, 3):
            s = False
            break
    return s


part1 = part2 = 0
data = open(0).read().splitlines()

for r in data:
    ls = list(map(int, r.split()))

    part1 += is_safe(ls)
    if is_safe(ls):
        part2 += 1
        continue
    for i, l in enumerate(ls):
        ls1 = ls[:i] + ls[i + 1:]
        if is_safe(ls1):
            part2 += 1
            break

print(part1)
print(part2)
