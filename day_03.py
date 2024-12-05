# copy data to test.txt and in.txt
# aliases in terminal to run day_00.py:
#   'aot' for test, 'aos' for puzzle input, 'aoc' to run both

import re

pattern1 = re.compile(r"mul\(\d+,\d+\)")
pattern2 = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
part1 = part2 = 0
data = open(0).read().splitlines()

for s in data:
    m = re.findall(pattern1, s)
    for e in m:
        a, b = map(int, re.findall(r"\d+", e))
        part1 += a * b

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

print(part1)
print(part2)
