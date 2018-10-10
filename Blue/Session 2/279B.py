# http://codeforces.com/problemset/problem/279/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

total_time = 0

left = 0
right = 0

max_total_book = 0
max_left = 0

while True:

    while right < n and total_time + a[right] <= t:
        total_time += a[right]
        right += 1

    while total_time > t:
        total_time -= a[left]
        left += 1

    if right - left > max_total_book:
        max_total_book = right - left
        max_left = left

    if right < n:
        total_time += a[right]
        right += 1
    else:
        break

print(max_total_book)
