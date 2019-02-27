# Problem from SPOJ
# https://www.spoj.com/problems/UCV2013B/


INF = int(1e9)


def bellman_ford(N, M, E, q, case_number):
    dist = [INF for i in range(N + 1)]
    flag = [False for i in range(N + 1)]

    print('Case #' + str(case_number) + ':')

    dist[1] = 0
    for i in range(0, N-1):
        for j in range(M):
            u = E[j][0]
            v = E[j][1]
            w = E[j][2]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for j in range(M):
        u = E[j][0]
        v = E[j][1]
        w = E[j][2]
        if dist[u] != INF and dist[u] + w < dist[v]:
            flag[v] = True

    for cq in q:
        if flag[cq]:
            print('NEGATIVE CYCLE')
        elif dist[cq] == INF:
            print('NOT REACHABLE')
        else:
            print(dist[cq])


def solution():
    counter = 1
    while True:
        N = int(input())
        if N == 0:
            break

        E = []
        monuments = ['' for i in range(N)]
        for x in range(N):
            line = input().split()
            monuments[x] = line[0]
            for i in range(1, N + 1):
                if int(line[i]) != 0:
                    E.append([x, i - 1, int(line[i])])

        nq = int(input())
        q = []
        for x in range(nq):
            q.append(int(input()))

        bellman_ford(N, len(E), E, q, counter + 1)
        counter += 1


solution()


