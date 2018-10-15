# Problem from Codeforces
# http://codeforces.com/problemset/problem/602/B

n = int(input())
a = list(map(int, input().split()))

left, right = 0, 0
max_almost_constant_range = 1
evaluating_range = 1
range_max = a[0]
range_min = a[0]

while True:
    if right >= n - 1:
        break
    right += 1
    if a[right] > range_max and range_max - range_min >= 1:
        range_max = a[right]
        if max_almost_constant_range <= evaluating_range:
            max_almost_constant_range = evaluating_range
        evaluating_range = 1
        for i in range(right - 1, left - 1, -1):
            if a[i] == range_min:
                left = i + 1
                range_min += 1
                break
            evaluating_range += 1
    elif a[right] < range_min and range_max - range_min >= 1:
        range_min = a[right]
        if max_almost_constant_range <= evaluating_range:
            max_almost_constant_range = evaluating_range
        evaluating_range = 1
        for i in range(right - 1, left - 1, -1):
            if a[i] == range_max:
                left = i + 1
                range_max -= 1
                break
            evaluating_range += 1
    else:
        if a[right] > range_max:
            range_max = a[right]
        elif a[right] < range_min:
            range_min = a[right]
        evaluating_range += 1
        if max_almost_constant_range < evaluating_range:
            max_almost_constant_range = evaluating_range
print(max_almost_constant_range)
