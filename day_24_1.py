filename = "test.txt"
# filename = "in.txt"
with open(filename, "r") as f: data = f.read()

part1 = part2 = 0

inputs, blocks = data.split("\n\n")
gates = {}
results = {}
for line in inputs.splitlines():
    k, v = line.split(":")
    gates[k] = ("con", 1, 1, int(v))

for line in blocks.splitlines():
    i1, op, i2, _, out = line.split()
    gates[out] = [op, i1, i2, None]

print(gates)
while True:
    for out, (op, i1, i2, state) in gates.items():
        if state is None:
            if gates[i1][3] is None: continue
            if gates[i2][3] is None: continue
            i1, i2 = gates[i1][3], gates[i2][3]
            if op == "AND":
                state = i1 and i2
            elif op == "OR":
                state = i1 or i2
            elif op == "XOR":
                state = i1 != i2
            gates[out][3] = state
            if out.startswith("z"):
                results[out] = state

    if all(g[3] is not None for g in gates.values()): break

print(sorted(results.items()))
part1 = sum(s * 2 ** i for i, (z, s) in enumerate(sorted(results.items())))
print(part1)
