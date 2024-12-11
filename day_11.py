# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re

# data = "0 1 10 99 999"
# data = "125 17"
data = "1750884 193 866395 7 1158 31 35216 0"
data = list(map(int, re.findall("\d+", data)))


# # only managed part1 by myself like this:
# def apply_rules(n) -> list:
#     if n == 0: return [1]
#     digits = len(str(n))
#     if digits % 2 == 0:
#         return [int(str(n)[:digits // 2]), int(str(n)[digits // 2:])]
#     return [n * 2024]
#
#
# def one_blink(line: list) -> list:
#     new_list = []
#     for n in line:
#         new_list += apply_rules(n)
#     return new_list
#
#
# part1 = 0
# for n in data:
#     line = [n]
#     for i in range(25):
#         line = one_blink(line)
#     part1 += len(line)
#
# print(part1)  # 231278


# count down the steps_to_go
# follow recursively each stone(number)


# part 2 only with help and (self-made) cache like this:
def line_length(n: int, steps_to_go: int) -> int:
    # at the end of each branch is a single number
    if steps_to_go == 0: return 1

    steps_to_go -= 1
    # rule 1
    if n == 0:
        key = (1, steps_to_go)
        if key not in cache: cache[key] = line_length(*key)
        return cache[key]

    # rule 2
    d = len(str(n))
    if d % 2 == 0:  # rule 2
        l, r = int(str(n)[:d // 2]), int(str(n)[d // 2:])
        key1, key2 = (l, steps_to_go), (r, steps_to_go)
        if key1 not in cache: cache[key1] = line_length(*key1)
        if key2 not in cache: cache[key2] = line_length(*key2)
        return cache[key1] + cache[key2]

    # rule 3
    key = (n * 2024, steps_to_go)
    if key not in cache: cache[key] = line_length(*key)
    return cache[key]


cache = {}
part1: int = sum(line_length(n, 25) for n in data)
part2: int = sum(line_length(n, 75) for n in data)

print(part1)  # 231278
print(part2)  # 274229228071551
