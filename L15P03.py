n, x = map(int, input().split())
g_matrix = [list(map(int, input().split())) for i in range(n)]
degX = 0
for i in range(n):
    degX += g_matrix[x][i]
print(degX)
