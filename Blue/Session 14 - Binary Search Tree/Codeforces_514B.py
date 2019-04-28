# Problem from Codeforces
# http://codeforces.com/problemset/problem/514/B


def solution():
    n, x0, y0 = map(int, input().strip().split())
    shots = set()
    for i in range(n):
        x, y = map(int, input().strip().split())
        x, y = x - x0, y - y0
        angle = 1e4
        if y != 0:
            angle = x / y
        shots.add(angle)

    print(len(shots))


solution()
