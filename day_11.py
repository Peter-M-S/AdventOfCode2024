# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re

# only managed part1


def apply_rules(n) -> list:
    if n == 0: return [1]
    digits = len(str(n))
    if digits % 2 == 0:
        return [int(str(n)[:digits // 2]), int(str(n)[digits // 2:])]
    return [n * 2024]


def one_blink(line: list) -> list:
    new_list = []
    for n in line:
        new_list += apply_rules(n)
    return new_list


part1 = part2 = 0
# data = "0 1 10 99 999"
# data = "125 17"
data = "1750884 193 866395 7 1158 31 35216 0"
data = list(map(int, re.findall("\d+", data)))

for n in sorted(data):
    line = [n]
    for i in range(25):
        line = one_blink(line)
    part1 += len(line)

print(part1)    # 231278

print(part2)
