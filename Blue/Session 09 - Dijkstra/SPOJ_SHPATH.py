#  Problem from SHPATH
#  https://www.spoj.com/problems/SHPATH/


import heapq
import sys


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(n, s, d, graph):

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

    return dist[d]


def solution():

    s = int(input())

    for i in range(s):
        new_line = input().strip()
        if not new_line:
            n = int(input())
        else:
            n = int(new_line)
        cities_index = {}
        graph = [[] for xx in range(n + 1)]
        for xxx in range(n):

            cities_index[input()] = xxx + 1

            n_road = int(input())
            for r in range(n_road):
                ct, we = map(int, input().strip().split())
                graph[xxx + 1].append(Node(ct, we))

        num_roads = int(input())
        for nr in range(num_roads):
            st, ds = map(str, input().strip().split())

            print(dijkstra(n, cities_index[st], cities_index[ds], graph))


solution()
