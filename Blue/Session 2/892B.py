# Problem from Codeforces
# http://codeforces.com/problemset/problem/892/B

n = int(input())
L = list(map(int, input().split()))

total_people = n
last_kill = 0
for i in range(n - 1, 0, -1):
    if L[i] > last_kill:
        if L[i] < i:
            total_people -= (L[i] - last_kill)
            last_kill = L[i] - 1
        else:
            total_people -= i
            break
    else:
        last_kill = last_kill - 1 if last_kill > 0 else 0
print(total_people)
