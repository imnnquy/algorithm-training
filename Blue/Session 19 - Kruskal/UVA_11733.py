# Problem from UVA
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2833


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


def kruskal(number_of_cities, airport_cost):
    graph.sort(key=lambda _edge: _edge.weight)
    i = 0
    mst = 0
    n_airports = number_of_cities
    while len(dist) != number_of_cities - 1 and i < len(graph):
        edge = graph[i]
        i += 1
        u = find_set(edge.source)
        v = find_set(edge.target)
        if u != v:
            dist.append(edge)
            union_set(u, v)
            if edge.weight < airport_cost:
                n_airports -= 1
                mst += edge.weight

    return mst + n_airports * airport_cost, n_airports


def solution():

    T = int(input())

    for t in range(T):
        global graph, dist
        graph = []
        dist = []
        N, M, A = map(int, input().split())

        for _ in range(M):
            x, y, z = map(int, input().split())
            graph.append(Triad(x, y, z))

        make_set(N)

        cost, n_airports = kruskal(N, A)

        print('Case #{0}: {1} {2}'.format(t + 1, cost, n_airports))


solution()
