#  Problem from SPOJ
#  https://www.spoj.com/problems/UCV2013H/


import queue


def calc_slick(N, M, matrix):

    total_slicks = 0

    slick_list = {}

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for row_counter in range(N):
        for col_counter in range(M):
            if matrix[row_counter][col_counter] == 1:
                total_slicks += 1
                slick_size = 1
                q = queue.Queue()
                q.put([row_counter, col_counter])
                matrix[row_counter][col_counter] = 0
                while not q.empty():
                    checking_node = q.get()
                    for l in range(4):
                        neighbor_x = checking_node[0] + dx[l]
                        neighbor_y = checking_node[1] + dy[l]
                        if 0 <= neighbor_x < N and 0 <= neighbor_y < M and matrix[neighbor_x][neighbor_y] == 1:
                            q.put([neighbor_x, neighbor_y])
                            slick_size += 1
                            matrix[neighbor_x][neighbor_y] = 0

                if slick_size in slick_list:
                    slick_list[slick_size] += 1
                else:
                    slick_list[slick_size] = 1

    results = [[total_slicks]]

    for key in sorted(slick_list):
        results.append([key, slick_list[key]])

    return results


def solution():

    results = []
    while True:
        N, M = map(int, input().split())
        if N == 0:
            break
        matrix = []
        for i in range(N):
            matrix.append(list(map(int, input().split())))

        results.append(calc_slick(N, M, matrix))

    for i in range(len(results)):
        for j in range(len(results[i])):
            print(*results[i][j], sep=' ')


solution()
