# Problem from SPOJ
# https://www.spoj.com/problems/OPCPIZZA/


def solution():
    T = int(input())
    for i in range(T):
        n, m = map(int, input().strip().split())
        friends = list(map(int, input().strip().split()))
        friends.sort()
        left = 0
        right = n - 1
        total = 0
        while left < right:
            if friends[left] + friends[right] == m:
                left += 1
                right -= 1
                total += 1
            if friends[left] + friends[right] > m:
                right -= 1
            if friends[left] + friends[right] < m:
                left += 1

        print(total)


solution()


