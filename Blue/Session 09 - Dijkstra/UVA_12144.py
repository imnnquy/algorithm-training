#  Problem from UVA
#  https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3296


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


def dijkstra(n, s, graph, matrix):

    dist = [-1 for x in range(n)]
    path = [-1 for y in range(n)]
    pqueue = []
    heapq.heappush(pqueue, Node(s, 0))
    dist[s] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if matrix[u][neighbor.id] != -1:
                if w + neighbor.dist < dist[neighbor.id] or dist[neighbor.id] == -1:
                    dist[neighbor.id] = w + neighbor.dist
                    heapq.heappush(pqueue, Node(neighbor.id, dist[neighbor.id]))
                    path[neighbor.id] = u

    return [dist, path]


def solution():

    while True:
        n = int(inp.next())
        if n == 0:
            break
        m = int(inp.next())
        s = int(inp.next())
        d = int(inp.next())
        graph = [[] for i in range(n)]
        rev_graph = [[] for i in range(n)]
        matrix = [[-1 for i in range(n)] for j in range(n)]
        rev_matrix = [[-1 for i in range(n)] for j in range(n)]
        for i in range(m):
            A = int(inp.next())
            B = int(inp.next())
            W = int(inp.next())

            matrix[A][B] = W
            rev_matrix[B][A] = W

            graph[A].append(Node(B, W))
            rev_graph[B].append(Node(A, W))

        from_s = dijkstra(n, s, graph, matrix)
        from_d = dijkstra(n, d, rev_graph, rev_matrix)

        dist_from_s = from_s[0]
        dist_from_d = from_d[0]

        shortest = dist_from_s[d]

        if shortest == -1:
            print(-1)
            continue

        for i in range(n):
            if dist_from_d[i] + dist_from_s[i] == shortest:
                matrix[s][i] = -1
                matrix[i][d] = -1

        shortest = dijkstra(n, s, graph, matrix)[0][d]

        print(shortest)


solution()
