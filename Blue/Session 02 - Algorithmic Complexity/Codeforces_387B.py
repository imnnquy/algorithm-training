# Problem from Codeforces
# http://codeforces.com/problemset/problem/387/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

needed_problem_index = 0
prepared_problem_index = 0

while True:

    while prepared_problem_index < m and b[prepared_problem_index] < a[needed_problem_index]:
        prepared_problem_index += 1

    if prepared_problem_index >= m:
        break

    prepared_problem_index += 1

    needed_problem_index += 1

    if prepared_problem_index >= m:
        break

    if needed_problem_index >= n:
        break

print(n - needed_problem_index)
