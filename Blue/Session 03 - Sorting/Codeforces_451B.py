# Problem from Codeforces
# http://codeforces.com/problemset/problem/451/B

n = int(input())
a = list(map(int, input().split()))

found_decreasing_segment = False
start_segment = 0
end_segment = 0

i = 0
while i < n - 1:
    if a[i] > a[i + 1]:
        if found_decreasing_segment:
            print('no')
            exit()
        start_segment = i
        found_decreasing_segment = True
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1
        end_segment = i
        if (end_segment < n - 1 and a[start_segment] > a[end_segment + 1]) \
                or (start_segment > 0 and a[end_segment] < a[start_segment - 1]):
            print('no')
            exit()
    else:
        i += 1

print('yes')
print(start_segment + 1, end_segment + 1, sep=' ')
