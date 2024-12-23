import networkx as nw

# PART 1 and 2 quite slow, but working

# filename = "test.txt"
filename = "in.txt"
with open(filename, "r") as f: data = f.read()

part1 = part2 = 0

edges = set(tuple(line.split("-")) for line in data.splitlines())
G = nw.Graph(edges)

cores = []
for game in nw.simple_cycles(G, 3):
    if any(n[0] == "t" for n in game):
        cores.append(set(game))
        part1 += 1

nodes, best = set(G.nodes), set()
for core in cores:
    for n in nodes-core:
        if all({(n, c), (c, n)}.intersection(edges) for c in core): core.add(n)
    if len(core) > len(best): best = core

part2 = ",".join(sorted(best))

print(part1)    # 1400
print(part2)    # am,bc,cz,dc,gy,hk,li,qf,th,tj,wf,xk,xo
