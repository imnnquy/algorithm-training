# Problem from Codeforces
# http://codeforces.com/problemset/problem/677/A


def cal_road_width(_a, _h):
    road_width = 0
    for ai in _a:
        road_width += 1 if ai <= _h else 2
    return road_width


n, h = map(int, input().split())
a = list(map(int, input().split()))
print(cal_road_width(a, h))

