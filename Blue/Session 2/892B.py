# Problem from Codeforces
# http://codeforces.com/problemset/problem/892/B

n = int(input())
L = list(map(int, input().split()))

total_people = n
start_to_kill = n - 1

for i in range(n - 1, -1, -1):
    if start_to_kill >= i - 1:
        start_to_kill = i - 1
    for j in range(start_to_kill, -1, -1):
        if j >= i - L[i]:
            total_people -= 1
            start_to_kill = j - 1
        else:
            start_to_kill = j
            break
    if start_to_kill <= 0:
        break
print(total_people)
