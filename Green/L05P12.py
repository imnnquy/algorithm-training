n, k = map(int, input().split())
a = list(map(int, input().split()))
total_pass = 0
for i in range(0, n):
    total_pass += 1 if a[i] >= a[k - 1] and a[i] > 0 else 0
print(total_pass)
