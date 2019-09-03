#  Problem from LightOJ
#  http://lightoj.com/volume_showproblem.php?problem=1174


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


def dijkstra(n, S, T, graph):

    dist = [-1 for x in range(n+1)]
    pqueue = []
    heapq.heappush(pqueue, Node(S, 0))
    dist[S] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id] or dist[neighbor.id] == -1:
                dist[neighbor.id] = w + neighbor.dist
                heapq.heappush(pqueue, Node(neighbor.id, dist[neighbor.id]))
            if neighbor.id == T:
                return dist[neighbor.id]


def solution():

    T = int(inp.next())
    results = []
    case_number = 0

    for i in range(T):
        case_number += 1
        N = int(inp.next())
        R = int(inp.next())
        graph = [[] for i in range(N + 1)]
        for j in range(R):
            A = int(inp.next())
            B = int(inp.next())

            graph[B].append(Node(A, 1))
            graph[A].append(Node(B, 1))

        s = int(inp.next())
        d = int(inp.next())

        mx = 0
        for j in range(N):
            p = dijkstra(N, s, j, graph)
            q = dijkstra(N, j, d, graph)
            mx = max(mx, p + q)

        results.append('Case ' + str(case_number) + ': ' + str(mx))

    print(*results, sep='\n')


solution()
