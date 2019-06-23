# Problem from LightOJ
# http://lightoj.com/volume_showproblem.php?problem=1041


import heapq


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def prim(N, graph):

    dist = [-1 for x in range(N+1)]
    visited = [False for i in range(N + 1)]
    pqueue = []
    heapq.heappush(pqueue, Node(1, 0))
    dist[1] = 0

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and (w < dist[v] or dist[v] == -1):
                dist[v] = w
                heapq.heappush(pqueue, Node(v, w))

    result = 0
    for i in range(1, N + 1):
        if dist[i] != -1:
            result += dist[i]
        else:
            return 'Impossible'

    return str(result)


def solution():

    t = int(input())
    for j in range(t):
        input()
        m = int(input())
        graph = [[] for i in range(m * 2 + 1)]
        cities = {}
        index = 0
        for i in range(m):
            city1, city2, cost = map(str, input().strip().split())
            if cities.get(city1) is None:
                index += 1
                cities[city1] = index
            if cities.get(city2) is None:
                index += 1
                cities[city2] = index
            cost = int(cost)
            graph[cities[city1]].append(Node(cities[city2], cost))
            graph[cities[city2]].append(Node(cities[city1], cost))

        result = prim(len(cities), graph)

        print('Case {}: {}'.format(j + 1, result))


solution()

