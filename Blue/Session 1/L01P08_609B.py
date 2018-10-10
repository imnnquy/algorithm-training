n, m = map(int, input().split())
a = list(map(int, input().split()))

total = 0
type_list = [0] * m
for i in range(n):
    type_list[a[i] - 1] += 1
for j in range(m - 1):
    for k in range(j + 1, m):
        total += type_list[j] * type_list[k]
print(total)