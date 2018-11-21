# Problem from Codeforces
# http://codeforces.com/problemset/problem/580/C


import queue


def can_reach_destination(starting_point, ending_point, n, m, matrix):

    return 'YES'


def solution():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input().split())

    starting_point = list(map(int, input().split()))
    ending_point = list(map(int, input().split()))

    print(can_reach_destination(starting_point, ending_point, n, m, matrix))


solution()


