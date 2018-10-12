# Problem from Codeforces
# http://codeforces.com/problemset/problem/430/B


def destroy_balls(_a, _b, _x):
    if len(_a) == 0 or len(_b) == 0:
        return 0
    lenb = len(_b)
    a_cur_index = len(_a) - 1
    b_cur_index = 0
    if _a[a_cur_index] == _b[b_cur_index]:
        to_be_destroyed = 2
        a_cur_index -= 1
        b_cur_index += 1
        while a_cur_index >= 0:
            if _a[a_cur_index] == _x:
                to_be_destroyed += 1
                a_cur_index -= 1
            else:
                break
        while b_cur_index < lenb:
            if _b[b_cur_index] == _x:
                to_be_destroyed += 1
                b_cur_index += 1
            else:
                break
        if to_be_destroyed > 2:
            return to_be_destroyed + destroy_balls(_a[0:a_cur_index + 1], _b[b_cur_index:], _a[a_cur_index])
        else:
            return 0

    return 0


n, k, x = map(int, input().split())
c = list(map(int, input().split()))

cur_max = 0
for i in range(n - 1):
    if c[i] == x and c[i] == c[i + 1]:
        tmp_a = c[0:i+1]
        tmp_b = c[i+1:n]
        tmp_a.append(x)
        i += 1
        tmp_max = destroy_balls(tmp_a, tmp_b, x)
        if tmp_max > cur_max:
            cur_max = tmp_max
if cur_max >= 2:
    cur_max -= 1
else:
    cur_max = 0
print(cur_max)
