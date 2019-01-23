#  Problem from UVA
#  https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=370


import heapq

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

    return dist[T]


def solution():

    N = int(input().strip())
    for tc in range(N):
        dictionary = []
        while True:
            new_word = input().strip()
            if not new_word:
                continue
            if new_word == '*':
                break
            dictionary.append(new_word)

        queries = []
        while True:
            new_query = input().strip()
            if not new_query:
                break
            queries.append(list(map(str, new_query.split())))

        n_words = len(dictionary)
        n_queries = len(queries)
        graph = [[] for i in range(n_words)]
        for i in range(n_words):
            for j in range(i, n_words):
                if len(dictionary[i]) == len(dictionary[j]):
                    diff = 0
                    w_length = len(dictionary[i])
                    for c in range(w_length):
                        if dictionary[i][c] is not dictionary[j][c]:
                            diff += 1
                        if diff > 1:
                            break

                    if diff == 1:
                        graph[i].append(Node(j, 1))
                        graph[j].append(Node(i, 1))

        for q in range(n_queries):
            start = -1
            end = -1
            for w in range(n_words):
                if start >= 0 and end >= 0:
                    break
                if queries[q][0] == dictionary[w]:
                    start = w
                if queries[q][1] == dictionary[w]:
                    end = w

            print(queries[q][0], queries[q][1], dijkstra(n_words, start, end, graph), sep=' ')


solution()
