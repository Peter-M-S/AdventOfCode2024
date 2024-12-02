import os
from time import perf_counter as pfc
from tools.AOC_input import get_input

DAY: int = int(os.path.basename(__file__)[4:6])


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


def solve(data: list, part1=False, part2=False):
    for r in data:
        ls = list(map(int, r.split()))

        part1 += is_safe(ls)
        if is_safe(ls):
            part2 += 1
            continue
        for i, l in enumerate(ls):
            ls1 = ls[:i]+ls[i+1:]
            if is_safe(ls1):
                part2 += 1
                break
    return part1, part2


def main(example):

    if example:
        with open("example.txt") as f:
            data = f.read().split("\n")
    else:
        data: list = get_input(DAY)

    start = pfc()
    print(*solve(data))
    print(f"{((pfc() - start) * 1000):5.1f} ms")
    # part2 435 too low , 5?? too high


if __name__ == '__main__':
    # main(True)
    main(False)
