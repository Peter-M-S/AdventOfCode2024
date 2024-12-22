# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re
import math
part1 = part2 = 0
# grid = open(0).read().splitlines()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()
machines = [list(map(int, re.findall("\d+", s))) for s in data.split("\n\n")]
presses = []
# for ax, ay, bx, by, px, py in machines:
#     found = False
#     na = 0
#     while not found:
#         if na > 100: break
#         nb = 0
#         while not found:
#             if nb > 100: break
#             if na * ax + nb * bx == px and na * ay + nb * by == py:
#                 presses.append((na, nb))
#                 found = True
#             nb += 1
#             if nb > 100 or na > 100: exceeded = True
#         na += 1
#     # print(presses)
# part1 = sum(na * 3 + nb for na, nb in presses)
#
# print(part1)


# Alternative
print()
print("Alternative")
presses = []
for ax, ay, bx, by, px, py in machines:
    # X: if ax>3*bx : cost to move x by A is cheaper
    # Y: if ay>3*by : cost to move y by A is cheaper
    first_direction = (ax, bx)
    if ax<3*bx:
        first_direction = (bx, ax)

    else:




    # >1 favour A, <1 favour B
    # x_ratio = ax / (3 * bx)
    # y_ratio = ay / (3 * by)

    # px += 10000000000000
    # py += 10000000000000

    lcm_x = math.lcm(ax, bx)
    lcm_y = math.lcm(ay, by)
    # print(lcm_x, lcm_y)

    # find solution for x with max A:
    na = px // ax  # max steps of ax to px,
    nb = 0
    na_r = px % ax  # 0 <= na_r < ax
    if na_r == 0:  # for x only A needed
        pass

    if na_r > 0:  # need to reduce na to match any*nb
        while na_r % bx > 0:
            na -= 1
            na_r += ax
            if na_r > lcm_x: break
            nb = na_r // bx

    print(f"na: {na}   nb: {nb}")
    if na * ax + nb * bx == px:  # solution found for x
        print(f"first solution for x is {na}, {nb}")
        second = True
        while na * ay + nb * by != py and second:  # solution also for y => final solution
            na -= lcm_x // ax
            if na<0 : second = False
            print(f"first solution for x is {na}, {nb}")
            nb += lcm_x // bx
        if second:
            print(f"solution is {na}, {nb} ")
            presses.append((na, nb))
        else:
            print("no solution")
    else:
        print("no solution for na")

    print()
part2 = sum(na * 3 + nb for na, nb in presses)
print(part2)
