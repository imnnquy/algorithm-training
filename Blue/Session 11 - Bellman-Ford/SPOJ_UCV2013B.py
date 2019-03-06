# Problem from SPOJ
# https://www.spoj.com/problems/UCV2013B/

from collections import defaultdict

INF = int(1e9)


def bellman_ford(N, M, E, query):
    dist = [INF for i in range(N + 1)]
    flag = [False for i in range(N + 1)]

    dist[query] = 0
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
            dist[v] = dist[u] + w
            flag[v] = True

    return [dist, flag]


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
                    if int(line[i]) < 0 or x != i - 1:
                        E.append([x, i - 1, int(line[i])])

        nq = int(input())
        q = []
        queries = defaultdict(list)
        for x in range(nq):
            pair = list(map(int, (input().split())))
            q.append(pair)
            queries[pair[0]].append(pair[1])

        print('Case #' + str(counter) + ':')

        dists = [[] for x in range(N)]
        neg_flags = [[] for x in range(N)]

        for query in queries.keys():
            bf_result = bellman_ford(N, len(E), E, query)
            dists[query] = bf_result[0]
            neg_flags[query] = bf_result[1]

        for qq in q:
            dist = dists[qq[0]][qq[1]]
            is_neg = neg_flags[qq[0]][qq[1]]
            if (dist < 0 and qq[0] == qq[1]) or is_neg:
                print("NEGATIVE CYCLE")
            else:
                if dist == INF:
                    dist = "NOT REACHABLE"
                start_city = monuments[qq[0]]
                dest_city = monuments[qq[1]]
                print("{}-{} {}".format(start_city, dest_city, dist))

        counter += 1


solution()


