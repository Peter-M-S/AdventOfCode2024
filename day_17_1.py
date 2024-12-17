# AoC2024 Day 17 Part 1
import re


def adv(op, pointer, output):
    REG[4] = int(REG[4] / (2 ** REG[op]))
    return pointer + 2, output


def bdv(op, pointer, output):
    REG[5] = int(REG[4] / (2 ** REG[op]))
    return pointer + 2, output


def cdv(op, pointer, output):
    REG[6] = int(REG[4] / (2 ** REG[op]))
    return pointer + 2, output


def bxl(op, pointer, output):
    REG[5] = REG[5] ^ op
    return pointer + 2, output


def bst(op, pointer, output):
    REG[5] = REG[op] % 8
    return pointer + 2, output


def jnz(op, pointer, output):
    if REG[4]: return op, output       # with op==0 prog will loop until A==0
    return pointer, output      # not jumping, looping in jnz = halt


def bxc(op, pointer, output):
    REG[5] = REG[5] ^ REG[6]
    return pointer + 2, output


def out(op, pointer, output):
    output.append(REG[op] % 8) # can be 0-7, if 0==REG[op] is divisible by 8 else not
    return pointer + 2, output


def call_prog(prog, pointer=0):
    output = []
    last_pointer = 0
    while True:
        opc, opr = prog[pointer:pointer + 2]
        func = CMD[opc]
        pointer, output = func(opr, pointer, output)
        # print(f"{prog[last_pointer]}({opr})-> {REG[4]:8d} {REG[5]:8d} {REG[6]:8d} -> {output[-1] if output else '[]'}")
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
