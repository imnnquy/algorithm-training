m, n = map(int, input().split())
a, b, p = map(int, input().split())
matrix = [[0 for i in range(n)] for j in range(m)]
matrix[0][0] = a
matrix[0][1] = b
for i in range(2, m * n):
    matrix[i // n][i % n] = (matrix[(i - 1) // n][(i - 1) % n] + matrix[(i - 2) // n][(i - 2) % n]) % p
for i in range(m):
    print(*matrix[i], sep=' ')
