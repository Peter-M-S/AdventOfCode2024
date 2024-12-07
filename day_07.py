# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import itertools
import re

part1 = part2 = 0
data = open(0).read().splitlines()
# with open("in.txt", "r") as f: data = f.readlines()
# with open("test.txt", "r") as f: data = f.readlines()

ops = ["*", "+", "|"]

for j, line in enumerate(data):
    # print(j)
    res, *vals = re.findall("\d+", line)
    res = int(res)
    ops_n = len(vals) - 1
    cache: dict = dict()

    configs = ["".join(c) for c in itertools.product(ops[:2], repeat=ops_n)]
    for config in configs:
        right = int(vals[0])
        key = config
        while key:
            if key in cache:    # found the longest existing key for this config
                right = cache[key]
                config = config[len(key):]
                break
            key = key[:-1]

        for o, v in zip(config, vals[len(key)+1:]):
            right = eval(str(right) + o + v)
            key += o
            cache[key] = right
            if right > res: break   # cannot find a solution above res

        if right == res:
            part1 += res
            break

    configs = ["".join(c) for c in itertools.product(ops, repeat=ops_n)]
    for config in configs:
        right = int(vals[0])
        key = config
        while key:
            if key in cache:    # found the longest existing key for this config
                right = cache[key]
                config = config[len(key):]
                break
            key = key[:-1]

        for o, v in zip(config, vals[len(key)+1:]):
            right = int(str(right)+v) if o == "|" else eval(str(right) + o + v)
            key += o
            cache[key] = right
            if right > res: break   # cannot find a solution above res

        if right == res:
            part2 += res
            break

print(part1)    # 4364915411363
print(part2)    # 38322057216320
