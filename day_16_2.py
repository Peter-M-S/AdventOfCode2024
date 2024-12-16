# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both
from collections import defaultdict, deque
from heapq import heappush, heappop

part2 = 0
# data = open(0).readlines()
# with open("test.txt", "r") as f: data = f.readlines()
with open("in.txt", "r") as f: data = f.readlines()


grid = [line.strip() for line in data]
START = [(r, line.index("S")) for r, line in enumerate(grid) if "S" in line]

min_cost, finales = float("inf"), set()

q = []
heappush(q, (0, *START, 0, 1))  # priority queue: cost,r,c,dr,dc
costs = defaultdict(int)
costs[(*START, 0, 1)] = 0
predecessors = defaultdict(set)
predecessors[(*START, 0, 1)] = set()

while q:
    cost, r, c, dr, dc = heappop(q)
    # do "processing" here
    if cost > costs.get((r, c, dr, dc), float("inf")): continue     # found better state already

    if grid[r][c] == "E":
        if cost > min_cost: break
        # first finisher will be definitely the cheapest and set min_cost,
        # then follow all other best, then the worse
        min_cost = cost
        print("found E", cost, dr, dc)
        finales.add((r, c, dr, dc))       # might arrive from different directions

    # find next moves (follow (dr, dc), turn CW, turn CCW)
    for ncost, nr, nc, ndr, ndc in ((cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)):
        if grid[nr][nc] == "#": continue

        least_cost = costs.get((nr, nc, ndr, ndc), float("inf"))
        if least_cost < ncost: continue
        if least_cost > ncost:                                  # if n is  better than others
            predecessors[(nr, nc, ndr, ndc)] = set()
            costs[(nr, nc, ndr, ndc)] = ncost
        predecessors[(nr, nc, ndr, ndc)].add((r, c, dr, dc))    # if n is same as best, add more predecessors

        heappush(q, (ncost, nr, nc, ndr, ndc))

# use predecessors for reconstruction of paths by bfs from E to S
states = deque(finales)
seats = set(finales)

while states:
    this_state = states.popleft()
    for previous in predecessors.get(this_state, []):
        if previous in seats: continue
        seats.add(previous)          # en passant collecting all states af all cheapest paths
        states.append(previous)

part2 = len({(r, c) for r, c, *_ in seats})






print(part2)  # found 12 best paths
