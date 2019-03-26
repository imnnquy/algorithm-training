# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=508


INF = float(1e9)
MAXN = 26


def floyd_warshall(youngGraph, oldGraph, start_young, start_old):
    for k in range(MAXN):
        for i in range(MAXN):
            for j in range(MAXN):
                youngGraph[i][j] = min(youngGraph[i][j], youngGraph[i][j] + youngGraph[k][j])
                oldGraph[i][j] = min(oldGraph[i][j], oldGraph[i][j] + oldGraph[k][j])

    min_dist, min_i = INF, -1
    for i in range(MAXN):
        d = youngGraph[start_young][i] + oldGraph[start_old][i]
        if d < min_dist:
            min_dist, min_i = d, i
    if min_dist >= INF:
        print('You will never meet.')
    else:
        print('{:d} {:s}'.format(min_dist, chr(ord('A') + min_i)))


def solution():
    while True:
        N = int(input().strip())
        if N == 0:
            break

        youngGraph = [[INF] * MAXN for i in range(MAXN)]
        oldGraph = [[INF] * MAXN for i in range(MAXN)]

        streets = []
        for i in range(N):
            line = list(map(str, input().strip().split()))

            if line[0] == 'Y':
                x = ord(line[2]) - 65
                y = ord(line[3]) - 65
                youngGraph[x][y] = int(line[-1])
                if line[1] == 'B':
                    youngGraph[y][x] = int(line[-1])
            else:
                x = ord(line[2]) - 65
                y = ord(line[3]) - 65
                oldGraph[x][y] = int(line[-1])
                if line[1] == 'B':
                    oldGraph[y][x] = int(line[-1])

        start_young, start_old = map(lambda x: ord(x) - 65, input().strip().split())

        floyd_warshall(youngGraph, oldGraph, start_young, start_old)


solution()


