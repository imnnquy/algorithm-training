# BLUE_LEC18P03

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

    t = 1
    while True:
        n, m = map(int, input().split())
        if m == 0 and n == 0:
            break

        make_set(n)

        for i in range(m):
            x, y = map(int, input().split())
            union_set(x, y)

        religion_leaders = dict()

        for i in range(1, n + 1):
            leader = find_set(i)
            if religion_leaders.get(leader) is not None:
                religion_leaders[leader] += 1
            else:
                religion_leaders[leader] = 1

        print("Case {0}: {1}".format(t, len(religion_leaders)))
        t += 1


solution()

