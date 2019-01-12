import heapq


class Node:
    def __init__(self, idx, idy, dist):
        self.dist = dist
        self.idx = idx
        self.idy = idy

    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(r, c, s, d, matrix):

    dist = [[-1 for x in range(c)] for y in range(r)]
    pqueue = []
    heapq.heappush(pqueue, Node(s[0], s[1], 0))
    dist[s[0]][s[1]] = 0

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while len(pqueue) > 0:
        top = heapq.heappop(pqueue)
        u = top.idx
        v = top.idy
        w = top.dist
        for ll in range(4):
            neighbor_x = u + dx[ll]
            neighbor_y = v + dy[ll]
            if 0 <= neighbor_x < r and 0 <= neighbor_y < c and matrix[neighbor_x][neighbor_y] == False:
                if w + 1 < dist[neighbor_x][neighbor_y] or dist[neighbor_x][neighbor_y] == -1:
                    dist[neighbor_x][neighbor_y] = w + 1
                    heapq.heappush(pqueue, Node(neighbor_x, neighbor_y, dist[neighbor_x][neighbor_y]))

    return dist[d[0]][d[1]]


def solution():
    while True:
        R, C = map(int, input().strip().split())
        if R == 0:
            break

        boom_rows = int(input())

        matrix = [[False for i in range(C)] for j in range(R)]

        for i in range(boom_rows):
            booms = list(map(int, input().strip().split()))
            for j in range(2, booms[1] + 2):
                matrix[booms[0]][booms[j]] = True

        s = list(map(int, input().strip().split()))
        d = list(map(int, input().strip().split()))
        print(dijkstra(R, C, s, d, matrix))


solution()
