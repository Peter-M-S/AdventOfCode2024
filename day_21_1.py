# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
import re
from collections import deque, defaultdict
import itertools


# PART1, for PART2 this is too slow
part1 = part2 = 0
# data = open(0).read()
# with open("test.txt", "r") as f: data = f.read()
with open("in.txt", "r") as f: data = f.read()

nkp = ["789", "456", "123", "_0A"]
dkp = ["_^A", "<v>"]

n_pos = {s: (r, c) for r, row in enumerate(nkp) for c, s in enumerate(row) if s != "_"}
d_pos = {s: (r, c) for r, row in enumerate(dkp) for c, s in enumerate(row) if s != "_"}


def get_shortest(pos: dict) -> dict:
    shorts = defaultdict(list)  # d_shots[from_a, to_b] = [list of possible shortest sequences]
    for p1 in pos:
        for p2 in pos:
            if p1 == p2:
                shorts[p1, p2] = ["A"]
                continue
            q = deque([(pos[p1], "")])
            min_length = 1000
            found_shortest = False
            while q and not found_shortest:
                (r, c), s = q.popleft()
                for nr, nc, ns in ((r - 1, c, s + "^"), (r, c + 1, s + ">"), (r + 1, c, s + "v"), (r, c - 1, s + "<")):
                    if (nr, nc) not in pos.values(): continue
                    if (nr, nc) == pos[p2]:
                        if len(ns) <= min_length:
                            min_length = len(ns)
                            if sum(ns.count(a) for a in ("^>", "^<", ">^", "<^", "v>", "v<", ">v", "<v")) > 1:
                                continue    # any path with more than one turn will result in longer path later
                            shorts[p1, p2].append(ns + "A")
                        else:
                            found_shortest = True
                            break

                    q.append(((nr, nc), ns))
    return shorts


n_shorts = get_shortest(n_pos)
# for k, v in n_shorts.items(): print(k, v)
d_shorts = get_shortest(d_pos)
# for k, v in d_shorts.items(): print(k, v)

# n_shorts = defaultdict(list)  # d_shots[from_a, to_b] = [list of possible shortest sequences]
# for d1 in n_pos:
#     for d2 in n_pos:
#         if d1 == d2:
#             n_shorts[d1, d2] = ["A"]
#             continue
#         q = deque([(n_pos[d1], "")])
#         min_length = 1000
#         found_shortest = False
#         while q and not found_shortest:
#             (r, c), s = q.popleft()
#             for nr, nc, ns in ((r - 1, c, "^"), (r, c + 1, ">"), (r + 1, c, "v"), (r, c - 1, "<")):
#                 if (nr, nc) not in n_pos.values(): continue
#                 if (nr, nc) == n_pos[d2]:
#                     if len(s + ns) <= min_length:
#                         min_length = len(s + ns)
#                         if sum(
#                             (s + ns).count(a) for a in ("^>", "^<", ">^", "<^", "v>", "v<", ">v", "<v")) > 1: continue
#                         n_shorts[d1, d2].append(s + ns + "A")
#                     else:
#                         found_shortest = True
#                         break
#
#                 q.append(((nr, nc), s + ns))
# for k, v in n_shorts.items(): print(k, v)

# n_shorts = dict()
# n_shorts["7"] = {"8": "<", "9": "<<",
#                  "4": "^", "5": {"<^", "^<"}, "6": {"<<^", "^<<"},
#                  "1": "^^", "2": {"<^^", "^^<"}, "3": {"<<^^", "^^<<"},
#                  "0": "^^^<", "A": "^^^<<"
#                  }
# n_shorts["8"] = {"7": ">", "9": "<",
#                  "4": {">^", "^>"}, "5": "^", "6": {"<^", "^<"},
#                  "1": {">^^", "^^>"}, "2": "^^", "3": {"<^^", "^^<"},
#                  "0": "^^^", "A": {"^^^<", "<^^^^"}
#                  }
# n_shorts["9"] = {"7": ">>", "8": ">",
#                  "4": {">>^", "^>>"}, "5": {">^", "^>"}, "6": "^",
#                  "1": {">>^^", "^^>>"}, "2": {">^^", "^^>"}, "3": "^^",
#                  "A": "^^^", "0": {"^^^>", ">^^^^"}
#                  }
# n_shorts["4"] = {"7": "v", "8": {"<v", "v<"}, "9": {"<<v", "v<<"},
#                  "5": "<", "6": "<<",
#                  "1": "^", "2": {"<^", "^<"}, "3": {"<<^", "^<<"},
#                  "0": "^^<", "A": "^^<<"
#                  }
# n_shorts["5"] = {"7": {"v>", ">v"}, "8": "v", "9": {"<v", "v<"},
#                  "4": ">", "6": "<",
#                  "1": {">^", "^>"}, "2": "^", "3": {"<^", "^<"},
#                  "0": "^^", "A": {"<^^", "^^<"}
#                  }
# n_shorts["6"] = {"7": {"v>>", ">>v"}, "8": {"v>", ">v"}, "9": "v",
#                  "4": ">>", "5": ">",
#                  "1": {">>^", "^>>"}, "2": {">^", "^>"}, "3": "^",
#                  "0": {">^^", "^^>"}, "A": "^^"
#                  }
# n_shorts["1"] = {"7": "vv", "8": {"<vv", "vv<"}, "9": {"vv<<", "<<vv"},
#                  "4": "v", "5": {"v>", ">v"}, "6": {"<<v", "v<<"},
#                  "2": "<", "3": "<<",
#                  "0": "^<", "A": "^<<"
#                  }
# n_shorts["2"] = {"7": {"vv>", ">vv"}, "8": "vv", "9": {"<vv", "vv<"},
#                  "5": "v", "4": {"v>", ">v"}, "6": {"<v", "v<"},
#                  "1": ">", "3": "<",
#                  "0": "^", "A": {"<^", "^<"}
#                  }
# n_shorts["3"] = {"7": {"vv>>", ">>vv"}, "8": {"vv>", ">vv"}, "9": "<vv",
#                  "6": "v", "5": {"v>", ">v"}, "4": {"v>>", ">>v"},
#                  "1": ">>", "2": ">",
#                  "0": {">^", "^>"}, "A": "^"
#                  }
# n_shorts["0"] = {"7": ">vvv", "8": "vvv", "9": {"<vvv", "vvv<"},
#                  "5": "vv", "4": ">vv", "6": {"vv<", "<vv"},
#                  "1": ">v", "2": "v", "3": {"<v", "v<"},
#                  "A": "<"
#                  }
# n_shorts["A"] = {"7": ">>vvv", "8": {">vvv", "vvv>"}, "9": "vvv",
#                  "4": ">>vv", "5": {"vv>", ">vv"}, "6": "vv",
#                  "1": ">>v", "3": "v", "2": {"v>", ">v"},
#                  "0": ">"
#                  }

for code in data.splitlines():
    factor = int(re.findall(r"\d+", code)[0])
    print(factor)
    seqs_on_1 = []
    for s1, s2 in zip("A" + code, code):
        seqs_on_1.append(n_shorts[s1, s2])
    # print(seqs_on_1)
    shorts_on_1 = ["".join(x) for x in itertools.product(*seqs_on_1)]
    # print(shorts_on_1)

    shorts_on_last = shorts_on_1
    for robot in range(2):
        print("  ", robot)
        shorts_on_current = []
        for seq in shorts_on_last:
            seqs_on_current = []
            for s1, s2 in zip("A" + seq, seq):
                seqs_on_current.append(d_shorts[s1, s2])
            # print(seqs_on_2)
            shorts_on_current.extend(["".join(x) for x in itertools.product(*seqs_on_current)])
        # print(list(map(len, shorts_on_2)))
        shorts_on_last = shorts_on_current
    print("    ", min(map(len, shorts_on_last)))

    part1 += factor * min(map(len, shorts_on_last))

print(part1)  # 163086
print(part2)
