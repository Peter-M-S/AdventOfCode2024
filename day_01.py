# copy data to test.txt and in.txt
# aliases in terminal to run day_00.py:
#   'aot' for test, 'aos' for puzzle input, 'aoc' to run both

# part1 = part2 = 0
data = open(0).read().splitlines()

l1 = sorted([int(s.split()[0]) for s in data])
l2 = sorted([int(s.split()[1]) for s in data])
part1 = sum(abs(n - m) for n, m in zip(l1, l2))
part2 = sum(n * l2.count(n) for n in l1)

print(part1)
print(part2)
