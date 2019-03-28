# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1744
# import sys
import math

INF = float(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(M, towns):

    graph = [[INF] * M for i in range(M)]
    for i in range(M):
        for j in range(i + 1, M):
            pow2_dist = math.pow((towns[i][0] - towns[j][0]), 2) + math.pow((towns[i][1] - towns[j][1]), 2)
            if pow2_dist <= 100:
                graph[i][j] = math.sqrt(pow2_dist)
                graph[j][i] = math.sqrt(pow2_dist)

    for i in range(M):
        graph[i][i] = 0

    dist = [[INF] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            dist[i][j] = graph[i][j]

    for k in range(M):
        for i in range(M):
            for j in range(M):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    max_range = 0
    for i in range(M):
        for j in range(M):
            if dist[i][j] == INF:
                return 0
            if max_range < dist[i][j]:
                max_range = dist[i][j]

    return max_range


def solution():
    T = int(input().strip())
    for t in range(T):
        M = int(input().strip())
        towns = []
        for i in range(M):
            x, y = map(int, input().strip().split())
            towns.append([x, y])

        if t != 0:
            print()
        print('Case #' + str(t + 1) + ':')
        result = floyd_warshall(M, towns)
        if result > 0:
            print("{:.4f}".format(result))
        else:
            print('Send Kurdy')


solution()


