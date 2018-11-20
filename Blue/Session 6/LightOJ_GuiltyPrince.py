#  Problem from Light OJ
#  http://lightoj.com/volume_showproblem.php?problem=1012


import queue


def calculate_possible_cells(wi, hi, matrix, prince_position):
    total_possible_cells = 1
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False for i in range(wi)] for j in range(hi)]
    q = queue.Queue()
    q.put(prince_position)

    while not q.empty():
        checking_node = q.get()
        for i in range(4):
            neighbor_x = checking_node[0] + dx[i]
            neighbor_y = checking_node[1] + dy[i]
            if neighbor_x >= 0 and neighbor_y >= 0 and neighbor_x < hi and neighbor_y < wi and matrix[neighbor_x][neighbor_y] == '.':
                if not visited[neighbor_x][neighbor_y]:
                    q.put([neighbor_x, neighbor_y])
                    visited[neighbor_x][neighbor_y] = True
                    total_possible_cells += 1

    return total_possible_cells


def solution():
    results = []
    T = int(input())
    for i in range(T):
        Wi, Hi = map(int, input().split())
        matrix = []
        prince_position = []
        for j in range(Hi):
            new_line = input().strip()
            if new_line.find('@') >= 0:
                prince_position.append(j)
                prince_position.append(new_line.find('@'))
            matrix.append(new_line)
        results.append('Case {0}: {1}'.format(i + 1, calculate_possible_cells(Wi, Hi, matrix, prince_position)))

    print(*results, sep='\n')


solution()
