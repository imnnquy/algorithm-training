# Problem from URI
# https://www.urionlinejudge.com.br/judge/en/problems/view/1655


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


INF = -int(1e9)


def bellman_ford(n, m, E):
    dist = [INF for i in range(n + 1)]
    dist[1] = 100
    for i in range(1, n):
        for j in range(m):
            u = E[j][0]
            v = E[j][1]
            w = E[j][2]
            if dist[u] != INF and dist[u] * w / 100 > dist[v]:
                dist[v] = dist[u] * w / 100

    return "{:.6f}".format(dist[n]) + ' percent'


def solution():
    while True:
        n = int(inp.next())
        if n == 0:
            break
        m = int(inp.next())

        E = []
        for i in range(m):
            a = int(inp.next())
            b = int(inp.next())
            p = int(inp.next())
            E.append([a, b, p])
            E.append([b, a, p])

        print(bellman_ford(n, m * 2, E))


solution()


