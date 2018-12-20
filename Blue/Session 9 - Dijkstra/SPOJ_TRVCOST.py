#  Problem from SPOJ
#  https://www.spoj.com/problems/TRVCOST/


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


MAX = 1100


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(s, graph, queries):

    dist = [-1 for x in range(MAX)]
    path = [-1 for y in range(MAX)]
    pqueue = []
    heapq.heappush(pqueue, Node(s, 0))
    dist[s] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id] or dist[neighbor.id] == -1:
                dist[neighbor.id] = w + neighbor.dist
                heapq.heappush(pqueue, Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u

    results = []
    nqueries = len(queries)
    for i in range(nqueries):
        if dist[queries[i]] != -1:
            results.append(str(dist[queries[i]]))
        else:
            results.append('NO PATH')

    return results


def solution():

    N = int(inp.next())

    matrix = [[False for j in range(MAX)] for i in range(MAX)]

    graph = [[] for i in range(N)]
    for i in range(N):
        A = int(inp.next())
        B = int(inp.next())
        W = int(inp.next())
        if not matrix[A][B]:
            matrix[A][B] = True
            graph[A].append(Node(B, W))
            graph[B].append(Node(A, W))

    U = int(inp.next())
    Q = int(inp.next())
    queries = []
    for i in range(Q):
        queries.append(int(inp.next()))

    results = dijkstra(U, graph, queries)

    print(*results, sep='\n')


solution()
