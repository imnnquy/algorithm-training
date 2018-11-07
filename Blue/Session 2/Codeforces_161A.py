# Problem from Codeforces
# http://codeforces.com/problemset/problem/161/A

n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

u, v = [], []

sindex = 0
vindex = 0

while True:

    while vindex < m and a[sindex] - x > b[vindex]:  # too small
        vindex += 1  # Add vest's size

    if vindex >= m:
        break

    while sindex < n and a[sindex] + y < b[vindex]:  # too big
        sindex += 1  # Add solider's size

    if sindex >= n:
        break

    if a[sindex] - x > b[vindex]:
        continue

    u.append(sindex + 1)
    v.append(vindex + 1)

    sindex += 1
    vindex += 1

    if sindex >= n or vindex >= m:
        break

print(len(u))
for i in range(len(u)):
    print(u[i], v[i], sep=' ')
