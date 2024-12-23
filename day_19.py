from functools import cache

# filename = "test.txt"
filename = "in.txt"
with open(filename, "r") as f: data = f.read()

part1 = part2 = 0

patterns, designs = data.split("\n\n")
patterns = patterns.split(", ")
designs = designs.splitlines()


@cache
def can_display(design) -> int:
    v = 0
    if design == "": return 1
    for pattern in patterns:
        if design.startswith(pattern):
            v += can_display(design.removeprefix(pattern))
    return v


for design in designs:
    v = can_display(design)
    part1 += bool(v)
    part2 += v

print(part1)
print(part2)
