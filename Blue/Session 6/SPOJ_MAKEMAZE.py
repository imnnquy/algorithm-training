#  Problem from SPOJ
#  https://www.spoj.com/problems/MAKEMAZE/


import queue


def check_path(m, n, maze_matrix, start_point, end_point):

    return True


def get_edge_openings(m, n, maze_matrix):
    edge_openings_counter = 0
    edge_openings = []
    for i in range(m):
        if maze_matrix[i][0]:
            edge_openings_counter += 1
            edge_openings.append([i, 0])
        if n > 1 and maze_matrix[i][n - 1]:
            edge_openings_counter += 1
            edge_openings.append([i, n - 1])
        if edge_openings_counter > 2:
            return []

    for i in range(1, n - 1, 1):
        if maze_matrix[0][i]:
            edge_openings_counter += 1
            edge_openings.append([0, i])
        if m > 1 and maze_matrix[m - 1][i]:
            edge_openings_counter += 1
            edge_openings.append([m - 1, i])
        if edge_openings_counter > 2:
            return []

    return edge_openings


def check_valid_maze(m, n, maze_matrix):
    edge_openings = get_edge_openings(m, n, maze_matrix)
    if len(edge_openings) == 2:
        return check_path(m, n, maze_matrix, edge_openings[0], edge_openings[1])
    return False


def solution():
    t = int(input())
    result = []

    for i in range(t):
        m, n = map(int, input().split())
        M = []
        for row in range(m):
            M.append([])
            rowi = input().strip()
            for col in range(n):
                M[row].append(1 if rowi[col] == '.' else 0)
        result.append('valid' if check_valid_maze(m, n, M) else 'invalid')

    print(*result, sep='\n')


solution()
