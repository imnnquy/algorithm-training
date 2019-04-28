#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/description/


def check_exist(_in, _out):
    inside_class = set(_in)
    for stu in _out:
        if stu in inside_class:
            print('YES')
        else:
            print('NO')
        inside_class.add(stu)


def solution():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        inside_class = A[:N]
        outside_class = A[N:]
        check_exist(inside_class, outside_class)


solution()
