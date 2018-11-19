#  Problem from SPOJ
#  https://www.spoj.com/problems/MAKEMAZE/


import queue


def check_path(m, n, maze_graph, start_point, end_point):
    visited = [[False for i in range(n)] for j in range(m)]

    q = queue.Queue()
    visited[start_point[0]][start_point[1]] = True
    q.put(start_point)
    while not q.empty():
        u = q.get()
        for v in maze_graph[u[0]][u[1]]:
            if not visited[v[0]][v[1]]:
                if v[0] == end_point[0] and v[1] == end_point[1]:
                    return True
                visited[v[0]][v[1]] = True
                q.put(v)

    return False


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
        maze_graph = []
        for i in range(m):
            maze_graph.append([[] for l in range(n)])
            for j in range(n):
                if maze_matrix[i][j] == 1:
                    if i > 0 and maze_matrix[i - 1][j] == 1:
                        maze_graph[i][j].append([i - 1, j])
                    if j > 0 and maze_matrix[i][j - 1] == 1:
                        maze_graph[i][j].append([i, j - 1])
                    if i < m - 1 and maze_matrix[i + 1][j] == 1:
                        maze_graph[i][j].append([i + 1, j])
                    if j < n - 1 and maze_matrix[i][j + 1] == 1:
                        maze_graph[i][j].append([i, j + 1])
        return check_path(m, n, maze_graph, edge_openings[0], edge_openings[1])
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
