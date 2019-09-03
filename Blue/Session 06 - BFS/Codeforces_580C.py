# Problem from Codeforces
# http://codeforces.com/problemset/problem/580/C


import queue


def bfs_count_possible_leaves(n, m, a, graph):

    consecutive_cats = [-1 for i in range(n+9)]

    total_restaurants = 0

    consecutive_cats[1] = a[0]

    q = queue.Queue()
    q.put(1)

    while not q.empty():
        u = q.get()
        if len(graph[u]) == 1 and u != 1:
            total_restaurants += 1
        else:
            for v in graph[u]:
                if consecutive_cats[v] == -1:
                    if a[v-1] == 0:
                        consecutive_cats[v] = 0
                    else:
                        consecutive_cats[v] = consecutive_cats[u] + 1
                    if consecutive_cats[v] <= m:
                        q.put(v)
    return total_restaurants


def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for i in range(n + 1)]
    root = -1
    for i in range(1, n):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    print(bfs_count_possible_leaves(n, m, a, graph))


solution()


