# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=499


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


def bellman_ford(N, M, E):
    dist = [INF for i in range(N + 1)]

    dist[0] = 0
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
            return 'possible'

    return 'not possible'


def solution():
    T = int(inp.next())
    for t in range(T):
        N = int(inp.next())
        M = int(inp.next())
        E = []
        for m in range(M):
            i = int(inp.next())
            j = int(inp.next())
            C = int(inp.next())
            E.append([i, j, C])
        print(bellman_ford(N, M, E))


solution()


