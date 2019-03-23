# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1187
import sys

INF = int(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(M, graph, case_number, queries, feast_cost):
    dist = [[INF] * M for i in range(M)]
    worst_feast_costs = [[INF] * M for i in range(M)]
    for i in range(M):
        worst_feast_costs[i][i] = feast_cost[i]
    for i in range(M):
        for j in range(M):
            dist[i][j] = graph[i][j]
            max_feast_cost = max(worst_feast_costs[i][i], worst_feast_costs[j][j])
            worst_feast_costs[i][j] = max_feast_cost
            worst_feast_costs[j][i] = max_feast_cost

    for t in range(2):
        for k in range(M):
            for i in range(M):
                for j in range(M):
                    max_feast_cost = max(worst_feast_costs[i][k], worst_feast_costs[k][j])
                    if dist[i][j] + worst_feast_costs[i][j] > dist[i][k] + dist[k][j] + max_feast_cost:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        worst_feast_costs[i][j] = max_feast_cost

    print('Case #' + str(case_number))
    for i in range(len(queries)):
        cost = dist[queries[i][0] - 1][queries[i][1] - 1]
        if cost == INF:
            print(-1)
        else:
            print(cost + worst_feast_costs[queries[i][0] - 1][queries[i][1] - 1])


def solution():
    n_case = 1
    while True:

        line = input().strip()
        while not line:
            line = input().strip()
        C, R, Q = map(int, line.split())
        if C == 0:
            break
        if n_case != 1:
            print()
        feast_cost = list(map(int, input().strip().split()))

        graph = [[INF] * C for i in range(C)]
        for i in range(R):
            c1, c2, d = map(int, input().strip().split())
            graph[c1 - 1][c2 - 1] = d
            graph[c2 - 1][c1 - 1] = d

        queries = []
        for i in range(Q):
            query = list(map(int, input().strip().split()))
            queries.append(query)

        floyd_warshall(C, graph, n_case, queries, feast_cost)
        # print()
        n_case += 1


solution()


