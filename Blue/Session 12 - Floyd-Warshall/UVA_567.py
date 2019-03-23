# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=508
import sys

INF = int(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(M, graph, case_number, queries):
    dist = [[INF] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            dist[i][j] = graph[i][j]

    for k in range(M):
        for i in range(M):
            for j in range(M):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print('Test Set #' + str(case_number))
    for i in range(len(queries)):
        print("{:2d} to {:2d}: {:d}".format(queries[i][0], queries[i][1], dist[queries[i][0] - 1][queries[i][1] - 1]).rstrip('0'))


def solution():
    n_case = 1
    while True:
        M = 20
        graph = [[INF] * M for i in range(M)]
        for i in range(M - 1):
            try:
                line = list(map(int, input().strip().split()))
            except:
                return
            if len(line) == 0:
                return
            n_neighbor = line[0]
            for j in range(1, n_neighbor + 1):
                graph[i][line[j] - 1] = 1
                graph[line[j] - 1][i] = 1

        n_queries = int(input())
        queries = []
        for i in range(n_queries):
            query = list(map(int, input().strip().split()))
            queries.append(query)

        floyd_warshall(M, graph, n_case, queries)
        print()
        n_case += 1


solution()


