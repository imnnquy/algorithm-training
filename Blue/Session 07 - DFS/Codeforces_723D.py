# Problem from Codeforces
# http://codeforces.com/contest/723/problem/D


def fill_the_lakes(n, m, k, matrix):

    lakes = []

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            is_lake = False
            lake = []

            if matrix[i][j] == '.' and not visited[i][j]:
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    is_lake = False
                else:
                    is_lake = True
                lake.append([i, j])
                s = [[i, j]]
                visited[i][j] = True
                while len(s) > 0:
                    checking_node = s[-1]
                    s.pop()
                    for ll in range(4):
                        neighbor_x = checking_node[0] + dx[ll]
                        neighbor_y = checking_node[1] + dy[ll]
                        if 0 <= neighbor_x < n and 0 <= neighbor_y < m and matrix[neighbor_x][neighbor_y] == '.' and not visited[neighbor_x][neighbor_y]:
                            s.append([neighbor_x, neighbor_y])
                            lake.append([neighbor_x, neighbor_y])
                            visited[neighbor_x][neighbor_y] = True
                            if neighbor_x == 0 or neighbor_x == n - 1 or neighbor_y == 0 or neighbor_y == m - 1:
                                is_lake = False
            if is_lake and len(lake) > 0:
                lakes.append(lake)
    lakes = sorted(lakes, key=lambda _lake:len(_lake))

    to_be_filled = len(lakes) - k

    filled_cells = 0
    for i in range(to_be_filled):
        lake_len = len(lakes[i])
        for j in range(lake_len):
            matrix[lakes[i][j][0]][lakes[i][j][1]] = '*'
            filled_cells += 1

    print(filled_cells)
    for i in range(n):
        print(''.join(matrix[i]))


def solution():
    n, m, k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(input().strip()))

    fill_the_lakes(n, m, k, matrix)


solution()


