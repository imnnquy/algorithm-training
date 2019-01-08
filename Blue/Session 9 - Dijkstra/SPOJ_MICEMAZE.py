#  Problem from SPOJ
#  https://www.spoj.com/problems/MICEMAZE/


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


def dijkstra(E, T, N, graph):

    dist = [-1 for x in range(N+1)]
    path = [-1 for y in range(N+1)]
    pqueue = []
    heapq.heappush(pqueue, Node(E, 0))
    dist[E] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id] or dist[neighbor.id] == -1:
                dist[neighbor.id] = w + neighbor.dist
                heapq.heappush(pqueue, Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u

    result = 0
    for i in range(1, N+1):
        if 0 <= dist[i] <= T:
            result += 1

    return result


def solution():

    N = int(inp.next())
    E = int(inp.next())
    T = int(inp.next())
    M = int(inp.next())

    graph = [[] for i in range(N + 1)]
    for i in range(M):
        A = int(inp.next())
        B = int(inp.next())
        W = int(inp.next())

        graph[B].append(Node(A, W))

    result = dijkstra(E, T, N, graph)

    print(result)


solution()
