import os
from time import perf_counter as pfc
from aocd import get_data

YEAR: int = 2024
SESSIONS: dict = {
    2024: "53616c7465645f5f443f2f800c8db96badb87af3e6d39368ec46d18406a7659003fc4a7225a7202d64526ba5501b6160ac14875c4f4ff204dc215ebd8fa1a652"
}
DAY: int = int(os.path.basename(__file__)[4:6])


def solve(data, part1=False, part2=False):
    print(data)
    return part1, part2


def main(example):
    file_name = "example.txt" if example else os.path.basename(__file__)[:-3] + ".txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            print(f"{file_name} created")
            if not example:
                f.write(get_data(session=SESSIONS[YEAR], day=DAY, year=YEAR-1))
                print(f"puzzle input written to {file_name}")
    with open(file_name) as f:
        data = f.read().split("\n")

    # print(get_data(session=SESSIONS[YEAR], day=1, year=YEAR))

    start = pfc()
    print(*solve(data))
    print(f"{((pfc() - start) * 1000):5.1f} ms")


if __name__ == '__main__':
    # main(True)
    main(False)
