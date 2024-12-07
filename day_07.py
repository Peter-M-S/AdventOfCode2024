# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import itertools
import re

part1 = part2 = 0
data = open(0)
# with open("in.txt", "r") as f: data = f.readlines()
# with open("test.txt", "r") as f: data = f.readlines()

ops = (1, 2, 3)


def calc(r, o, v) -> int:
    if o == 1: return r * v
    if o == 2: return r + v
    return int(f"{r}{v}")


for j, line in enumerate(data):
    print(j)
    res, *vals = list(map(int, re.findall("\d+", line)))  # avoid str-operations
    ops_n = len(vals) - 1
    cache: dict = dict()

    configs = list(itertools.product(ops[:2], repeat=ops_n))
    for config in configs:
        r = vals[0]
        key = config
        while key:
            if key in cache:  # found the longest existing key for this config
                r = cache[key]
                config = config[len(key):]
                break
            key = key[:-1]

        for o, v in zip(config, vals[len(key) + 1:]):
            r = calc(r, o, v)
            key = tuple([*key, o])
            cache[key] = r
            if r > res: break  # cannot find a solution above res

        if r == res:
            part1 += res
            break

    configs = list(itertools.product(ops, repeat=ops_n))
    # keep the cache from part1
    for config in configs:
        r = int(vals[0])
        key = config
        while key:
            if key in cache:  # found the longest existing key for this config
                r = cache[key]
                config = config[len(key):]
                break
            key = key[:-1]

        for o, v in zip(config, vals[len(key) + 1:]):
            r = calc(r, o, v)
            key = tuple([*key, o])
            cache[key] = r
            if r > res: break  # cannot find a solution above res

        if r == res:
            part2 += res
            break

print(part1)  # 4364915411363
print(part2)  # 38322057216320
