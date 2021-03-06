#  Problem from UVA
#  https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1927


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


def dijkstra(n, S, T, graph, case_number):

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

    result = 'unreachable'
    if dist[T] >= 0:
        result = str(dist[T])

    return 'Case #' + str(case_number) + ': ' + result


def solution():

    N = int(inp.next())
    results = []
    case_number = 0

    for i in range(N):
        case_number += 1
        n = int(inp.next())
        m = int(inp.next())
        S = int(inp.next())
        T = int(inp.next())
        graph = [[] for i in range(n + 1)]
        for i in range(m):
            A = int(inp.next())
            B = int(inp.next())
            W = int(inp.next())

            graph[B].append(Node(A, W))
            graph[A].append(Node(B, W))

        results.append(dijkstra(n, S, T, graph, case_number))

    print(*results, sep='\n')


solution()
