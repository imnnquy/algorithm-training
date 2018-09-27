n = int(input())
g_matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(i, n):
        if g_matrix[i][j] != g_matrix[j][i]:
            print('NO')
            exit()
print('YES')
