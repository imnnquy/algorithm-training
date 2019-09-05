# Problem from Codeforces
# http://codeforces.com/problemset/problem/468/B


parent = []
ranks = []


def make_set(N):
    global parent, ranks
    parent = [i for i in range(N + 5)]
    ranks = [0 for i in range(N + 5)]


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    else:
        parent[u] = u
    return parent[u]


def union_set(u, v):
    up = find_set(u)
    vp = find_set(v)

    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


def solution():
    set_indicators = dict()
    n, a, b = map(int, input().split())
    numbers = list(map(int, input().split()))
    A = n + 1
    B = A + 1

    make_set(n)
    for i in range(n):
        set_indicators[numbers[i]] = i

    for i in range(n):
        if set_indicators.get(a - numbers[i]) is not None:
            union_set(i, set_indicators.get(a - numbers[i]))
        else:
            union_set(i, B)
        if set_indicators.get(b - numbers[i]) is not None:
            union_set(i, set_indicators.get(b - numbers[i]))
        else:
            union_set(i, A)
    if find_set(A) == find_set(B):
        print('NO')
        return

    print('YES')
    for i in range(n):
        print(1 if find_set(i) == find_set(n + 2) else 0)


solution()
