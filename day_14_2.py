# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re


def show_grid(positions, rows, cols):
    for r in range(rows):
        for c in range(cols):
            s = f"{positions.count((r, c))}" if (r, c) in positions else "."
            if r == rows // 2 or c == cols // 2: s = " "
            print(s, end="")
        print(end="\n")
    print()


part1 = part2 = 0
# data = open(0).read().splitlines()
# with open("test.txt", "r") as f: data = f.read().splitlines()
with open("in.txt", "r") as f: data = f.read().splitlines()

robots = [list(map(int, re.findall(r"-?\d+", line))) for line in data]

rows, cols = 103, 101

center_c, center_r = (cols - 1) // 2, (rows - 1) // 2

q_min = float("inf")
q_max = 0
result = []

for time in range(cols * rows):
    q1 = q2 = q3 = q4 = 0
    positions = []

    for c, r, dc, dr in robots:
        nc = (c + dc * time) % cols
        nr = (r + dr * time) % rows

        positions.append((nr, nc))

        if nr < center_r and nc < center_c:
            q1 += 1
        elif nr < center_r and nc > center_c:
            q2 += 1
        elif nr > center_r and nc < center_c:
            q3 += 1
        elif nr > center_r and nc > center_c:
            q4 += 1

    safety_factor = q1 * q2 * q3 * q4
    if time == 100:
        part1 = safety_factor

    # symmetry like (r,c) == (r, cols-1-c): is not working, tree is not necessarily in center

    # if max(q1, q2, q3, q4) > q_max:   # 'most robots in a quadrant' is not working
    #     q_max = max(q1, q2, q3, q4)
    #     print(q_max, time)
    #     show_grid(positions, rows, cols)
    #     result = time, positions

    if len(set(positions)) == len(positions):  # this iw working but for no reason in the text
        print("no doubles")
        show_grid(positions, rows, cols)
        result = time, positions

    # if safety_factor < q_min:         # 'lowest safety factor' is not working
    #     q_min = safety_factor
    #     print(q_min, time)
    #     # show_grid(positions, rows, cols)
    #     result = time, positions

part2 = result[0]
show_grid(result[1], rows, cols)
print(part1)  # 232253028
print(part2)  # 8179 (Xmas tree overlapping center_r)
