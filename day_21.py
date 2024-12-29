# with help from https://github.com/LiquidFun/adventofcode/blob/main/2024/21/21.py
from functools import cache

part1 = part2 = 0

# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

nkp = ["789", "456", "123", "_0A"]
dkp = ["_^A", "<v>"]

n_pos = {s: (r, c) for r, row in enumerate(nkp) for c, s in enumerate(row)}  # if s != "_"}
d_pos = {s: (r, c) for r, row in enumerate(dkp) for c, s in enumerate(row)}  # if s != "_"}


@cache
def get_s1_to_s2(s1: str, s2: str) -> str:
    keypad = n_pos if s1 in n_pos and s2 in n_pos else d_pos
    r1, c1 = keypad[s1]
    r2, c2 = keypad[s2]
    dr, dc = r2 - r1, c2 - c1
    path_r = "v" * dr if dr > 0 else "^" * abs(dr)
    path_c = ">" * dc if dc > 0 else "<" * abs(dc)

    dr_bad = keypad['_'][0] - r1
    dc_bad = keypad['_'][1] - c1

    # todo this condition is SOMEHOW not enough to avoid blank and prefer vertical first
    # if (r1 + dr, c1) not in keypad.values():  # moving row first will not land keypad
    #     return path_c + path_r + "A"
    # return path_r + path_c + "A"

    # This condition is needed for correct result:
    row_first = (dc > 0 or (dr_bad, dc_bad) == (0, dc)) and (dr_bad, dc_bad) != (dr, 0)
    if row_first: return path_r + path_c + "A"
    return path_c + path_r + "A"


@cache
def dfs_sequence(sequence, robots) -> int:       # needs to pass only int, str is too slow
    if robots < 0: return len(sequence)
    n_seq = 0
    for s1, s2 in zip("A" + sequence, sequence):
        n_seq += dfs_sequence(get_s1_to_s2(s1, s2), robots-1)
    return n_seq


for code in data.splitlines():
    robots = 2
    factor = int(code[:3])
    sequence = dfs_sequence(code, robots)  # need to pass "remaining robots", to cache correct level
    part1 += factor * sequence
print(f"{part1=}")  # 163086

for code in data.splitlines():
    robots = 25
    factor = int(code[:3])
    sequence = dfs_sequence(code, robots)
    part2 += factor * sequence
print(f"{part2=}")  # 198466286401228
