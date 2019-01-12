
def solution():
    k, n, w = map(int, input().strip().split())

    result = int((w + 1) * w * k / 2 - n)
    if result < 0:
        result = 0

    print(result)


solution()
