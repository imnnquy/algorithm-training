# Problem from Codeforces
# http://codeforces.com/problemset/problem/600/B


def binary_search(arr, val, left, right):
    if right > left + 1:
        if val >= arr[(right - left) // 2 + left]:
            return binary_search(arr, val, (right - left) // 2 + left, right)
        else:
            return binary_search(arr, val, left, (right - left) // 2 + left)

    return right + 1 if (right < len(arr) and val >= arr[right]) else left + 1


def solution():
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a.sort()

    for i in range(m - 1):
        print(binary_search(a, b[i], -1, n), end=' ')
    print(binary_search(a, b[m-1], -1, n))


solution()
