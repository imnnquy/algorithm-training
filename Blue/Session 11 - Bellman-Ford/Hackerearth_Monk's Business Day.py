#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/description/


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

    dist[1] = 0
    for i in range(1, N):
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
            return 'Yes'

    return 'No'


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
            E.append([i, j, -C])
        print(bellman_ford(N, M, E))


solution()
