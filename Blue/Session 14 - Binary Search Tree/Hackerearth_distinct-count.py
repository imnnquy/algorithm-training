#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/


def check_distinct(_n, _x, _a):
    distinct_set = set(_a)
    # for i in range(_n):
    #     distinct_set.add(_a[i])
    if len(distinct_set) == _x:
        return 'Good'
    if len(distinct_set) < _x:
        return 'Bad'
    return 'Average'


def solution():
    T = int(input())
    for i in range(T):
        N, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        print(check_distinct(N, X, A))


solution()
