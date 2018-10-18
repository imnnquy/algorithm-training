# Problem from Codeforces
# http://codeforces.com/problemset/problem/169/A

n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

print(h[b] - h[b - 1])
