# Problem from Codeforces
# http://codeforces.com/problemset/problem/702/B


def solution():
    n = int(input())
    a = list(map(int, input().split()))

    pow2 = [2 ** i for i in range(61)]

    total = 0
    dic = {}
    for i in range(n):
        for j in range(60):
            if pow2[j] - a[i] in dic:
                total += dic[pow2[j] - a[i]]

        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1

    print(total)


solution()
