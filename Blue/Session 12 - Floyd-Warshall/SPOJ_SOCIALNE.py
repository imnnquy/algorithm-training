# Problem from SPOJ
# https://www.spoj.com/problems/SOCIALNE/


INF = int(1e9)


def floyd_warshall(M, matrix):
    dist = [[False] * M for i in range(M)]
    for i in range(M):
        n_friend = 0
        for j in range(M):
            if matrix[i][j] == 'Y':
                n_friend += 1
                dist[i][j] = True

    n_more_friends = [0 for i in range(M)]
    for k in range(M):
        for i in range(M):
            for j in range(M):
                if not dist[i][j] and i != j and matrix[i][k] == 'Y' and matrix[k][j] == 'Y':
                    dist[i][j] = True
                    n_more_friends[i] += 1

    max_new_friends = n_more_friends[0]
    most_pop_person = 0
    for i in range(1, M):
        if n_more_friends[i] > max_new_friends:
            max_new_friends = n_more_friends[i]
            most_pop_person = i
    print(most_pop_person, max_new_friends)


def solution():
    T = int(input())
    for i in range(T):
        matrix = []
        first_line = input().strip()
        M = len(first_line)
        matrix.append(first_line)
        for j in range(M - 1):
            matrix.append(input().strip())

        floyd_warshall(M, matrix)


solution()


