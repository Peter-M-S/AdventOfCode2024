import re


def solve_2_unknowns(xa, ya, xb, yb, x0, y0):
    tol = 2
    A = round((y0 - (x0 * yb / xb)) / (ya - (xa * yb / xb)), tol)
    B = round((x0 - A * xa) / xb, tol)
    return A, B


# filename = "test.txt"
filename = "in.txt"
with open(filename, "r") as f: data = f.read()

part1 = part2 = 0

machines = [list(map(int, re.findall(r"\d+", s))) for s in data.split("\n\n")]

for m in machines:
    A, B = solve_2_unknowns(*m)
    if A % 1 or B % 1: continue
    if not (0 <= A <= 100 and 0 <= B <= 100): continue
    part1 += int(A) * 3 + int(B)

print(f"{part1= }")

delta = 10000000000000

for i in range(len(machines)):
    machines[i][4] += delta
    machines[i][5] += delta

for m in machines:
    A, B = solve_2_unknowns(*m)
    if A % 1 or B % 1: continue
    part2 += int(A) * 3 + int(B)

print(f"{part2= }")  # 104140871044942

