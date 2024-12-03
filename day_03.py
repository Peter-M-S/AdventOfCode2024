import os
from time import perf_counter as pfc
from tools.AOC_input import get_input
import re
DAY: int = int(os.path.basename(__file__)[4:6])

pattern1 = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
pattern2 = re.compile(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))")


def solve(data: list, part1=False, part2=False):
    for s in data:
        m = re.findall(pattern1, s)
        for e in m:
            a, b = map(int, re.findall(r"\d+", e))
            part1 += a*b

    enable = True
    for s in data:
        m = re.findall(pattern2, s)
        for e in m:
            if e in ("don't()", "do()"):
                enable = e == "do()"
                continue
            if enable:
                a, b = map(int, re.findall(r"\d+", e))
                part2 += a * b

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


if __name__ == '__main__':
    # main(True)
    main(False)
