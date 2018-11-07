# Problem from Codeforces
# http://codeforces.com/problemset/problem/149/A

k = int(input())
a = list(map(int, input().split()))

growth_cent = 0

a.sort(key=lambda x: -x)
for i in range(12):
    if growth_cent >= k:
        print(i)
        exit()
    growth_cent += a[i]
    if growth_cent >= k:
        print(i + 1)
        exit()

print('-1')
