# Problem from SPOJ
# https://www.spoj.com/problems/ARBITRAG/


INF = float(1e9)
# sys.stdout = open("file.txt", "w+")


def floyd_warshall(M, matrix):

    for k in range(M):
        for i in range(M):
            for j in range(M):
                if matrix[i][j] < matrix[i][k] * matrix[k][j]:
                    matrix[i][j] = matrix[i][k] * matrix[k][j]
    for i in range(M):
        if matrix[i][i] > 1:
            return 'Yes'

    return 'No'


def solution():
    n_case = 1
    while True:
        line = input().strip()
        while not line:
            line = input().strip()
        M = int(line)
        if M == 0:
            break

        my_dict = {}
        for i in range(M):
            my_dict[input().strip()] = i

        exchanges = int(input().strip())
        matrix = [[0.0] * M for i in range(M)]
        for i in range(exchanges):
            c1, rate, c2 = map(str, input().strip().split())
            matrix[my_dict[c1]][my_dict[c2]] = float(rate)

        print('Case ' + str(n_case) + ': ' + floyd_warshall(M, matrix))
        n_case += 1


solution()


