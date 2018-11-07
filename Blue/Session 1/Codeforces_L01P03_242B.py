# Problem from Codeforces
# http://codeforces.com/problemset/problem/242/B


def check_cover(_l, _r, _n):
    min_left, max_right = _l[0], _r[0]
    pos = 0
    for i in range(1, n):
        if _l[i] < min_left:
            min_left = _l[i]
            if _r[i] >= max_right:
                pos = i
                max_right = _r[i]
            else:
                pos = -2
        elif _r[i] > max_right:
            max_right = _r[i]
            if _l[i] <= min_left:
                pos = i
                min_left = _l[i]
            else:
                pos = -2
        elif _l[i] == min_left and _r[i] == max_right:
            pos = i

    return pos + 1


n = int(input())
l, r = [], []
for i in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
print(check_cover(l, r, n))
