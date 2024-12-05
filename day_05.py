# copy data to test.txt and in.txt
# aliases in terminal to run day_00.py:
#   'aot' for test, 'aos' for puzzle input, 'aoc' to run both


def swap(u: tuple, r: tuple) -> tuple:
    # swap the two elements of r in u
    result = list(u)
    i, j = u.index(r[0]), u.index(r[1])  # i > j because rule broken
    result.remove(r[1])
    result.remove(r[0])
    result.insert(j, r[0])  # insert lower index first
    result.insert(i, r[1])
    return tuple(result)


part1 = part2 = 0
rules, updates = open(0).read().split("\n\n")
rules = [tuple(r.split("|")) for r in rules.splitlines()]
updates = [tuple(u.split(",")) for u in updates.splitlines()]

incorrect_updates = []
for u in updates:
    if all(u.index(r[0]) < u.index(r[1]) for r in rules if set(r).issubset(u)):
        part1 += int(u[len(u)//2])
    else:
        incorrect_updates.append(u)

corrected_updates = []
for u in incorrect_updates:
    while not all(u.index(r[0]) < u.index(r[1]) for r in rules if set(r).issubset(u)):
        for r in rules:
            if not set(r).issubset(u): continue  # rule not used
            if u.index(r[0]) > u.index(r[1]):  u = swap(u, r)    # rule broken
    part2 += int(u[len(u)//2])

print(part1)
print(part2)
