# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364

INF = int(1e9)


def bellman_ford(N, M, E):
    dist = [INF for i in range(N)]

    dist[0] = 0
    for i in range(0, N-1):
        for j in range(M):
            u = E[j][0]
            v = E[j][1]
            w = E[j][2]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    max = 0
    for di in dist:
        if di > max:
            max = di

    return max


def solution():
    N = int(input())
    E = []
    for i in range(N - 1):
        line = list(map(str, input().strip().split()))
        for j in range(i + 1):
            if line[j] is not 'x':
                E.append([i + 1, j, int(line[j])])
                E.append([j, i + 1, int(line[j])])

    print(bellman_ford(N, len(E), E))


solution()


