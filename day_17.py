# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re


def adv(op, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[4] = res
    return pointer + 2, output


def bdv(op, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[5] = res
    return pointer + 2, output


def cdv(op, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[6] = res
    return pointer + 2, output


def bxl(op, pointer, output):
    res = REG[5] ^ op
    REG[5] = res
    return pointer + 2, output


def bst(op, pointer, output):
    res = REG[op] % 8
    REG[5] = res
    return pointer + 2, output


def jnz(op, pointer, output):
    if REG[4]:
        return op, output       # with op==0 prog will loop until A==0
    return pointer, output      # not jumping, looping in jnz = halt


def bxc(op, pointer, output):
    res = REG[5] ^ REG[6]
    REG[5] = res
    return pointer + 2, output


def out(op, pointer, output):
    res = REG[op] % 8           # res can be 0-7, if 0==REG[op] is divisible by 8 else not
    output.append(res)
    return pointer + 2, output


def call_prog(prog, pointer=0):
    output = []
    last_pointer = 0
    while True:
        opc, opr = prog[pointer:pointer + 2]
        func = CMD[opc]
        pointer, output = func(opr, pointer, output)

        print(f"{prog[last_pointer]}({opr})-> {REG[4]:8d} {REG[5]:8d} {REG[6]:8d} -> {output[-1] if output else '[]'}")

        if last_pointer == pointer and not REG[4]: break
        last_pointer = pointer

    return output


# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

A, B, C, *prog = map(int, (re.findall(r"\d+", data)))
REG = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: False}
CMD = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

part1 = ",".join(map(str, call_prog(prog, 0)))
print(part1)  # 6,2,7,2,3,1,6,0,5

# (((((0*8 + 3)*8 + 4)*8 + 5)*8 + 3)*8 + 0)*8 = 117440
# the example keeps dividing by 8 and outputs the remainder
#

part2 = ",".join(map(str, call_prog(prog)))
print(part2)
exit()


N = 0
for n in map(int, prog[::-1]):

    N = (N + n) * 8     # this modification is more complicated

# prog has 8 steps
# 1. bst(4): B = A % 8
# 2. bxl(3): B = B ^ 3
# 3. cdv(5): C = A // 32
# 4. bxl(5): B = B ^ 5
# 5. adv(3): A = A // 8
# 6. bxc(_): B = B ^ C
# 7. out(5): out = B % 8
# 8. jnz(0): repeat until A == 0

# Umkehrung von a = b % c:  b = x*c + a : min_b = a
# Umkehrung von a = b ^ c:  b = a ^ c
# Umkehrung von a = b // c: b = a * c
pointer = len(prog)-2
while prog:
    out = prog.pop()
    cmd = prog.pop()
    B = out     # 7.
    C =            # 6. zwei unbekannte?




REG = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: False}
print(N)
REG[4] = N
part2 = ",".join(map(str, call_prog(prog)))
print(part2)
