# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=400


parent = dict()
ranks = dict()


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


def solution():

    T = int(input())
    input()
    for t in range(T):
        n_nodes = ord(input()) - 64
        make_set(n_nodes)
        while True:
            try:
                line = input()
                u = ord(line[0]) - 65
                v = ord(line[1]) - 65
                union_set(u, v)
            except:
                break

        leaders = dict()
        for i in range(n_nodes):
            leader = find_set(i)
            if leaders.get(leader) is not None:
                leaders[leader] += 1
            else:
                leaders[leader] = 1

        print(len(leaders))
        if t != T - 1:
            print()


solution()
