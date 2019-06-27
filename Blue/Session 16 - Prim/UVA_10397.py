# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1338


import math
import heapq
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



class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def prim(N, graph):

    dist = [-1.0 for x in range(N+1)]
    visited = [False for i in range(N + 1)]
    pqueue = []
    heapq.heappush(pqueue, Node(0, 0))
    dist[0] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        visited[u] = True
        for i in range(N):
            v = i
            w = graph[u][i]
            if not visited[v] and w != -1 and (w < dist[v] or dist[v] == -1.0):
                dist[v] = w
                heapq.heappush(pqueue, Node(v, w))

    result = 0
    for i in range(N):
        if dist[i] != -1.0:
            result += dist[i]

    return result


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) * (city1[0] - city2[0]) + (city1[1] - city2[1]) * (city1[1] - city2[1]))


def solution():

    while True:
        try:
            n = int(inp.next())
        except:
            return
        cities = []
        for i in range(n):
            x = int(inp.next())
            y = int(inp.next())
            cities.append([x, y])
        graph = [[-1.0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(i + 1, n):
                distij = distance(cities[i], cities[j])
                graph[i][j] = distij
                graph[j][i] = distij

        m = int(inp.next())
        for i in range(m):
            x = int(inp.next())
            y = int(inp.next())
            graph[x - 1][y - 1] = 0
            graph[y - 1][x - 1] = 0

        result = prim(n, graph)

        print("{:.2f}".format(result))


solution()

