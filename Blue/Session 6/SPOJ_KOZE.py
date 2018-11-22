#  Problem from SPOJ
#  https://www.spoj.com/problems/KOZE/


import queue


def calc_survive(N, M, matrix):
    visited = [[False for i in range(M)] for j in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    wolfs_counter = 0
    sheeps_counter = 0

    for row_counter in range(N):
        for col_counter in range(M):
            if (matrix[row_counter][col_counter] == '.' or matrix[row_counter][col_counter] == 'k' or
                        matrix[row_counter][col_counter] == 'v') and not visited[row_counter][col_counter]:
                visited[row_counter][col_counter] = True
                q = queue.Queue()
                q.put([row_counter, col_counter])
                sheeps, wolfs = 0, 0
                if matrix[row_counter][col_counter] == 'k':
                    sheeps = 1
                if matrix[row_counter][col_counter] == 'v':
                    wolfs = 1
                belong_to_sector = True
                while not q.empty():
                    checking_node = q.get()
                    for l in range(4):
                        neighbor_x = checking_node[0] + dx[l]
                        neighbor_y = checking_node[1] + dy[l]
                        if 0 <= neighbor_x < N and 0 <= neighbor_y < M and (
                                            matrix[neighbor_x][neighbor_y] == '.' or matrix[neighbor_x][
                                        neighbor_y] == 'k' or
                                        matrix[neighbor_x][neighbor_y] == 'v') and not visited[neighbor_x][neighbor_y]:
                            q.put([neighbor_x, neighbor_y])
                            visited[neighbor_x][neighbor_y] = True
                            if matrix[neighbor_x][neighbor_y] == 'k':
                                sheeps += 1
                            if matrix[neighbor_x][neighbor_y] == 'v':
                                wolfs += 1
                            if neighbor_y == 0 or neighbor_x == 0 or neighbor_y == M - 1 or neighbor_x == N - 1:
                                belong_to_sector = False
                if belong_to_sector:
                    if sheeps > wolfs:
                        sheeps_counter += sheeps
                    else:
                        wolfs_counter += wolfs
                else:
                    sheeps_counter += sheeps
                    wolfs_counter += wolfs

    return [sheeps_counter, wolfs_counter]


def solution():
    while True:
        new_line = input().strip()
        if new_line:
            N, M = map(int, new_line.split())
            break
    backyard = []
    i = 0
    while i < N:
        new_line = input().strip()
        if new_line:
            backyard.append(new_line)
            i += 1

    print(*calc_survive(N, M, backyard), sep=' ')


solution()
