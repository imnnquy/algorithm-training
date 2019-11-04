# Problem from UVA
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3676


class Triad:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        return str(self.source) + '-' + str(self.target) + ': ' + str(self.weight)


parent = []
ranks = []
dist = []
graph = []


def make_set(V):
    global parent, ranks, dist
    parent = [i for i in range(V + 1)]
    ranks = [0 for _ in range(V + 1)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    up = find_set(u)
    vp = find_set(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


def kruskal(number_of_cities):
    graph.sort(key=lambda _edge: _edge.weight)
    i = 0
    mst = 0
    while len(dist) != number_of_cities - 1:
        edge = graph[i]
        i += 1
        u = find_set(edge.source)
        v = find_set(edge.target)
        if u != v:
            dist.append(edge)
            union_set(u, v)
            mst += edge.weight

    return mst


def calculate_rolls(start, stop):
    rolls = 0
    for i in range(4):
        sta, sto = int(start[i]), int(stop[i])
        rolls += min(abs(sta - sto), 10 - abs(sta - sto))

    return rolls


def solution():

    number_of_test_cases = int(input())

    for t in range(number_of_test_cases):
        global graph, dist
        graph = []
        dist = []
        line = input().split()
        number_of_locks = int(line[0])
        line[0] = '0000'
        initial = 100
        for i in range(1, number_of_locks + 1):
            initial = min(initial, calculate_rolls('0000', line[i]))
        for i in range(1, number_of_locks + 1):
            for j in range(i + 1, number_of_locks + 1):
                source = line[i]
                target = line[j]
                weight = calculate_rolls(source, target)
                graph.append(Triad(i, j, weight))

        make_set(number_of_locks)

        print(kruskal(number_of_locks) + initial)


solution()
