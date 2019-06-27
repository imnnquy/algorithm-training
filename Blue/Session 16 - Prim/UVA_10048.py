# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=989


INF = 1e9


def solution():

    index = 0
    while True:
        C, S, Q = map(int, input().strip().split())
        if C == 0:
            break
        if index > 0:
            print()
        graph = [[INF for j in range(C + 1)] for i in range(C + 1)]
        for i in range(S):
            A, B, W = map(int, input().strip().split())
            graph[A][B] = min(graph[A][B], W)
            graph[B][A] = min(graph[A][B], W)

        for k in range(1, C + 1):
            for i in range(1, C + 1):
                for j in range(1, C + 1):
                    graph[i][j] = min(graph[i][j], max(graph[i][k], graph[k][j]))

        index += 1
        print("Case #{}".format(index))
        for i in range(Q):
            s, e = map(int, input().strip().split())
            if graph[s][e] == INF:
                print('no path')
            else:
                print(graph[s][e])


solution()

