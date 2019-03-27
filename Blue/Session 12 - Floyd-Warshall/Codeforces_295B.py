# Problem from Codeforces
# http://codeforces.com/problemset/problem/295/B

import math

INF = float(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(N, matrix, del_list):

    ans = [0 for i in range(N + 1)]
    flag = [False for i in range(N + 1)]

    for k in range(N, 0, -1):
        c = del_list[k]
        for i in range(k + 1, N + 1):
            a = del_list[i]
            for j in range(k, N + 1):
                b = del_list[j]
                matrix[c][a] = min(matrix[c][a], matrix[c][b] + matrix[b][a])
                matrix[a][c] = min(matrix[a][c], matrix[a][b] + matrix[b][c])

        for i in range(k, N + 1):
            a = del_list[i]
            for j in range(k, N + 1):
                b = del_list[j]
                if a == b:
                    continue
                matrix[a][b] = min(matrix[a][b], matrix[a][c] + matrix[c][b])

        for i in range(k, N + 1):
            a = del_list[i]
            for j in range(k, N + 1):
                b = del_list[j]
                ans[k] += matrix[a][b]

    return ans[1:N+1]


def solution():
    N = int(input().strip())
    matrix = [[]]
    for i in range(N):
        new_line = [0] + list(map(int, input().strip().split()))
        matrix.append(new_line)

    del_list = [0] + list(map(int, input().strip().split()))

    print(*floyd_warshall(N, matrix, del_list), sep=' ')


solution()


