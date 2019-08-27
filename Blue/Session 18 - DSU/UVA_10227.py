# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1168


parent = []
ranks = []


def make_set(N):
    global parent, ranks
    parent = [i for i in range(N + 5)]
    ranks = [0 for i in range(N + 5)]


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


def has_same_opinion(opinions1, opinions2, length):
    for i in range(length):
        if opinions1[i] != opinions2[i]:
            return False
    return True


def solution():

    T = int(input())
    input()
    for t in range(T):

        P, T = map(int, input().split())

        opinions = [[False for i in range(T + 5)] for i in range(P + 5)]

        while True:
            try:
                line = input()
            except:
                break
            if not line:
                break
            try:
                p, t = map(int, line.split())
            except:
                break
            opinions[p][t] = True

        make_set(P)

        for i in range(1, P):
            for j in range(i + 1, P + 1):
                if has_same_opinion(opinions[i], opinions[j], T + 1):
                    union_set(i, j)

        opinions_set = dict()

        for i in range(1, P + 1):
            leader = find_set(i)
            if opinions_set.get(leader) is not None:
                opinions_set[leader] += 1
            else:
                opinions_set[leader] = 1

        print(len(opinions_set))
        print()


solution()

