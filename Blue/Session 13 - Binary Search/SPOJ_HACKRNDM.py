# Problem from SPOJ
# https://www.spoj.com/problems/HACKRNDM/


def binary_search(array, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if x == array[mid]:
            return True
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def solution():
    n, k = map(int, input().strip().split())
    random_numbers = list(map(int, input().strip().split()))
    random_numbers.sort()
    # print(random_numbers)
    total = 0
    n = len(random_numbers)

    for i in range(n):
        if binary_search(random_numbers, i+ 1, n - 1, random_numbers[i] + k):
            total += 1

    print(total)


solution()


