# Problem from LightOJ
# http://www.lightoj.com/volume_showproblem.php?problem=1074


import sys


class input_tokenizer:
    __tokens = None

    def has_next(self):
        return self.__tokens != [] and self.__tokens != None

    def next(self):
        token = self.__tokens[-1]
        self.__tokens.pop()
        return token

    def __init__(self):
        self.__tokens = sys.stdin.read().split()[::-1]


inp = input_tokenizer()


INF = int(1e9)


def bellman_ford(N, M, E, q):
    dist = [INF for i in range(N + 1)]
    flag = [False for i in range(N + 1)]

    dist[0] = 0
    for i in range(1, N):
        for j in range(M):
            u = E[j][0]
            v = E[j][1]
            w = E[j][2]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # for i in range(N):
    for j in range(M):
        u = E[j][0]
        v = E[j][1]
        w = E[j][2]
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            flag[v] = True

    for cq in q:
        if flag[cq]:
            print('-Infinity')
        elif dist[cq] == INF:
            print('Impossible')
        else:
            print(dist[cq])


def solution():
    while True:
        N = int(inp.next())
        if N == 0:
            break
        M = int(inp.next())
        Q = int(inp.next())
        S = int(inp.next())

        E = []
        for m in range(M):
            i = int(inp.next())
            j = int(inp.next())
            w = int(inp.next())
            E.append([i, j, w])
        q = []
        for x in range(Q):
            q.append(int(inp.next()))

        bellman_ford(N, M, E, q)
        print()


solution()


