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


def bellman_ford(N, M, E, q, case_number):
    dist = [INF for i in range(N + 1)]
    flag = [False for i in range(N + 1)]

    print('Case ' + str(case_number) + ':')

    dist[1] = 0
    for i in range(0, N-1):
        for j in range(M):
            u = E[j][0]
            v = E[j][1]
            w = E[j][2]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for j in range(M):
        u = E[j][0]
        v = E[j][1]
        w = E[j][2]
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            flag[v] = True

    for cq in q:
        if flag[cq] or dist[cq] < 3 or dist[cq] == INF:
            print('?')
        else:
            print(dist[cq])


def solution():
    T = int(inp.next())
    for t in range(T):
        N = int(inp.next())
        busyness = [0 for x in range(N + 1)]
        counter = 1
        for x in range(N):
            busyness[counter] = int(inp.next())
            counter += 1

        M = int(inp.next())
        E = []
        for m in range(M):
            i = int(inp.next())
            j = int(inp.next())
            E.append([i, j, busyness[j] - busyness[i]])
        nq = int(inp.next())
        q = []
        for x in range(nq):
            q.append(int(inp.next()))

        bellman_ford(N, M, E, q, t + 1)


solution()


