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


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(N, A, graph):

    dist = [-1 for x in range(N+1)]
    pqueue = []
    heapq.heappush(pqueue, Node(A, 0))
    dist[A] = 0

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

    N = int(inp.next())
    M = int(inp.next())
    k = int(inp.next())
    x = int(inp.next())

    chocolate_cities = []
    for i in range(k):
        chocolate_cities.append(int(inp.next()))

    graph = [[] for i in range(N + 1)]
    for i in range(M):
        A = int(inp.next())
        B = int(inp.next())
        W = int(inp.next())

        graph[B].append(Node(A, W))
        graph[A].append(Node(B, W))

    A = int(inp.next())
    B = int(inp.next())

    dist_from_b = dijkstra(N, B, graph)
    found_chocolate_city_to_b = False
    for i in range(k):
        if x >= dist_from_b[chocolate_cities[i]] >= 0:
            found_chocolate_city_to_b = True
            break

    if not found_chocolate_city_to_b:
        print(-1)
        return

    dist_from_a = dijkstra(N, A, graph)

    found_chocolate_city_to_a = False
    for i in range(k):
        if dist_from_a[chocolate_cities[i]] >= 0:
            found_chocolate_city_to_a = True
            break

    if not found_chocolate_city_to_a:
        print(-1)
        return

    min_time = -1

    for i in range(k):
        if x >= dist_from_b[chocolate_cities[i]] >= 0 and dist_from_a[chocolate_cities[i]] >= 0:
            if min_time == -1 or min_time > dist_from_b[chocolate_cities[i]] + dist_from_a[chocolate_cities[i]]:
                min_time = dist_from_b[chocolate_cities[i]] + dist_from_a[chocolate_cities[i]]

    print(min_time)


solution()
