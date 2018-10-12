# Problem from Codeforces
# http://codeforces.com/problemset/problem/224/B

n, k = map(int, input().split())
a = list(map(int, input().split()))

current_number = -1
total_distinct = 0

start_position = 0
end_position = -1

distinct_list = [0] * 100001

for i in range(n):
    if distinct_list[a[i]] == 0:
        total_distinct += 1
    distinct_list[a[i]] += 1
    if total_distinct == k:
        end_position = i
        break

if end_position == -1:
    print('-1 -1')
else:
    while True:
        if distinct_list[a[start_position]] > 1:
            distinct_list[a[start_position]] -= 1
            start_position += 1
        else:
            break
    print(start_position + 1, end_position + 1, sep=' ')
