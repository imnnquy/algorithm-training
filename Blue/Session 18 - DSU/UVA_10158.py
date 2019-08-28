# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1099


parent = []
ranks = []


def make_set(N):
    global parent, ranks
    parent = [i for i in range(2*N + 5)]
    ranks = [0 for i in range(2*N + 5)]


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

    n = int(input())
    make_set(n)
    while True:
        c, x, y = map(int, input().split())
        if c == 0:
            break
        if c == 1:
            if find_set(x) == find_set(y + n) or find_set(y) == find_set(x + n):
                print(-1)
            else:
                union_set(x, y)
                union_set(x + n, y + n)
        if c == 2:
            if find_set(x) == find_set(y) or find_set(x + n) == find_set(y + n):
                print(-1)
            else:
                union_set(x, y + n)
                union_set(y, x + n)
        if c == 3:
            if find_set(x) == find_set(y) or find_set(x + n) == find_set(y + n):
                print(1)
            else:
                print(0)
        if c == 4:
            if find_set(x) == find_set(y + n) or find_set(y) == find_set(x + n):
                print(1)
            else:
                print(0)


solution()

