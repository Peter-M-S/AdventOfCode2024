import os
from time import perf_counter as pfc
from aocd import get_data
from sessions import SESSIONS

YEAR: int = 2024
DAY: int = int(os.path.basename(__file__)[4:6])


def solve(data, part1=False, part2=False):
    l1 = sorted([int(s.split()[0]) for s in data])
    l2 = sorted([int(s.split()[1]) for s in data])
    part1 = sum(abs(n-m) for n,m in zip(l1,l2))
    part2 = 0
    for n in l1:
        part2 += n * l2.count(n)
    return part1, part2


def main(example):
    file_name = "example.txt" if example else os.path.basename(__file__)[:-3] + ".txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            print(f"{file_name} created")
            if not example:
                f.write(get_data(session=SESSIONS[YEAR], day=DAY, year=YEAR))
                print(f"puzzle input written to {file_name}")
    with open(file_name) as f:
        data = f.read().split("\n")

    start = pfc()
    print(*solve(data))
    print(f"{((pfc() - start) * 1000):5.1f} ms")


if __name__ == '__main__':
    # main(True)
    main(False)
