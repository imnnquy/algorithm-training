#  Problem from SPOJ
#  https://www.spoj.com/problems/TRAFFICN/


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


def dijkstra(n, s, graph):

    dist = [-1 for x in range(n + 1)]
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

    return dist


def solution():

    T = int(inp.next())

    for test_case in range(T):
        n = int(inp.next())
        m = int(inp.next())
        k = int(inp.next())
        s = int(inp.next())
        t = int(inp.next())
        graph = [[] for i in range(n + 1)]
        rev_graph = [[] for i in range(n + 1)]
        matrix = [[-1 for i in range(n+1)] for j in range(n+1)]
        for i in range(m):
            A = int(inp.next())
            B = int(inp.next())
            W = int(inp.next())

            matrix[A][B] = W

            graph[A].append(Node(B, W))
            rev_graph[B].append(Node(A, W))

        propose_roads = []
        for i in range(k):
            A = int(inp.next())
            B = int(inp.next())
            W = int(inp.next())

            propose_roads.append({"u": A, "v": B, "w": W})

        from_s = dijkstra(n, s, graph)
        from_t = dijkstra(n, t, rev_graph)

        minimum_path = -1

        for new_road in propose_roads:
            new_path = -1
            midle_weight = new_road['w']
            if 0 < matrix[new_road['u']][new_road['v']] < midle_weight:
                midle_weight = matrix[new_road['u']][new_road['v']]
            if from_s[new_road['u']] >= 0 and from_t[new_road['v']] >= 0:
                new_path = from_s[new_road['u']] + from_t[new_road['v']] + midle_weight

            if from_t[new_road['u']] >= 0 and from_s[new_road['v']] >= 0:
                new_path2 = from_t[new_road['u']] + from_s[new_road['v']] + midle_weight
                if new_path == -1 or new_path > new_path2:
                    new_path = new_path2

            if minimum_path == -1 or new_path < minimum_path:
                minimum_path = new_path

        if 0 < from_s[t] < minimum_path:
            minimum_path = from_s[t]
        print(minimum_path)


solution()
