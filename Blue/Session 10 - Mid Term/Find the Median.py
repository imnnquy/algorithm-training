
def solution():
    n = int(input())
    ar = list(map(int, input().strip().split()))
    ar.sort()
    mid_index = n//2

    print(ar[mid_index])


solution()
