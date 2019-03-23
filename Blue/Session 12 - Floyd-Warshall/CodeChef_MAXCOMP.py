# Problem from CodeChef
# https://www.codechef.com/problems/MAXCOMP
import sys

INF = int(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(M, graph):
    dist = [[0] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            dist[i][j] = graph[i][j]

    for x in range(5):
        for k in range(M):
            for i in range(M):
                for j in range(M):
                    if i <= k <= j and dist[i][j] < dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    max_comp = 0
    for i in range(M):
        for j in range(M):
            if max_comp < dist[i][j]:
                max_comp = dist[i][j]

    return max_comp


def solution():
    T = int(input().strip())
    M = 49
    for i in range(T):
        graph = [[0] * M for x in range(M)]
        N = int(input().strip())
        e_max = 0

        for j in range(N):
            si, ei, ci = map(int, input().strip().split())
            if ei > e_max:
                e_max = ei
            if ci > graph[si][ei]:
                graph[si][ei] = ci

        # Start of Simple solution
        mmax = [0 for x in range(M)]
        for x in range(1, e_max + 1):
            m = 0
            for xx in range(x):
                if m < graph[xx][x] + mmax[xx]:
                    m = graph[xx][x] + mmax[xx]
                mmax[x] = m

        print(mmax[e_max])
        # End of Simple solution

        # print(floyd_warshall(M, graph))


solution()


