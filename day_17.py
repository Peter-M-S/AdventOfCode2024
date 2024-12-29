import re


def adv(op, REG, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[4] = res
    return pointer + 2, output


def bdv(op, REG, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[5] = res
    return pointer + 2, output


def cdv(op, REG, pointer, output):
    res = int(REG[4] / (2 ** REG[op]))
    REG[6] = res
    return pointer + 2, output


def bxl(op, REG, pointer, output):
    res = REG[5] ^ op
    REG[5] = res
    return pointer + 2, output


def bst(op, REG, pointer, output):
    res = REG[op] % 8
    REG[5] = res
    return pointer + 2, output


def jnz(op, REG, pointer, output):
    if REG[4]:
        return op, output  # with op==0 prog will loop until A==0
    return pointer, output  # not jumping, looping in jnz = halt


def bxc(op, REG, pointer, output):
    res = REG[5] ^ REG[6]
    REG[5] = res
    return pointer + 2, output


def out(op, REG, pointer, output):
    res = REG[op] % 8  # res can be 0-7, if 0==REG[op] is divisible by 8 else not
    output.append(res)
    return pointer + 2, output


def call_prog(prog: list, regs) -> list:
    A, B, C = regs
    REG = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: False}
    output = []
    pointer = last_pointer = 0
    while True:
        opc, opr = prog[pointer:pointer + 2]
        func = CMD[opc]
        pointer, output = func(opr, REG, pointer, output)

        if last_pointer == pointer and not REG[4]: break
        last_pointer = pointer

    return output


def reversing(program, A, B, C, from_end) -> int:
    # recursively find modified A from end of program
    if len(program) - from_end < 0: return A   # 'from_end' is at start of program
    for i in range(8):
        output_start = call_prog(program, [A * 8 + i, B, C])[0]
        if output_start == program[-from_end]:
            # found the one option of i in [0:8] for start of output with this modified A
            # now test with modified A and previous step in program
            result = reversing(program, A * 8 + i, B, C, from_end + 1)
            if result: return result


# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

A, B, C, *prog = map(int, (re.findall(r"\d+", data)))
CMD = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

part1 = ",".join(map(str, call_prog(prog, [A, B, C])))
print(part1)  # 6,2,7,2,3,1,6,0,5

part2 = reversing(prog, 0, B, C, 1)
print(part2)    # 236548287712877
