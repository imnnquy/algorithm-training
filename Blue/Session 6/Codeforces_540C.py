# Problem from Codeforces
# http://codeforces.com/problemset/problem/580/C


import queue


def can_reach_destination(starting_point, ending_point, n, m, matrix):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False for i in range(m)] for j in range(n)]

    visited[starting_point[0]][starting_point[1]] = True

    q = queue.Queue()
    q.put(starting_point)
    while not q.empty():
        checking_node = q.get()
        for l in range(4):
            neighbor_x = checking_node[0] + dx[l]
            neighbor_y = checking_node[1] + dy[l]
            if neighbor_x == ending_point[0] and neighbor_y == ending_point[1]:
                if matrix[neighbor_x][neighbor_y] == 'X':
                    return 'YES'
                else:
                    for end_check in range(4):
                        end_neighbor_x = neighbor_x + dx[end_check]
                        end_neighbor_y = neighbor_y + dy[end_check]
                        if 0 <= end_neighbor_x < n and 0 <= end_neighbor_y < m and matrix[end_neighbor_x][end_neighbor_y] == '.':
                            if end_neighbor_x != checking_node[0] or end_neighbor_y != checking_node[1]:
                                return 'YES'
                    return 'NO'
            else:
                if 0 <= neighbor_x < n and 0 <= neighbor_y < m and matrix[neighbor_x][neighbor_y] == '.' and not visited[neighbor_x][neighbor_y]:
                    q.put([neighbor_x, neighbor_y])
                    visited[neighbor_x][neighbor_y] = True

    return 'NO'


def solution():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input().strip())

    starting_point = list(map(int, input().split()))
    ending_point = list(map(int, input().split()))

    starting_point[0] -= 1
    starting_point[1] -= 1
    ending_point[0] -= 1
    ending_point[1] -= 1

    print(can_reach_destination(starting_point, ending_point, n, m, matrix))


solution()


