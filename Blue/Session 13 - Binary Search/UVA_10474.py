# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1415
# import sys
import bisect

INF = float(1e9)
# sys.stdout = open("file.txt", "w+")


def solution():
    case = 1
    while True:
        N, Q = map(int, input().strip().split())

        if N == 0:
            break

        marbles = []
        for i in range(N):
            marbles.append(int(input().strip()))

        # sorted(marbles)
        marbles.sort()

        print('CASE# ' + str(case) + ':')
        for i in range(Q):
            q = int(input().strip())
            result = bisect.bisect_left(marbles, q)

            if 0 <= result < len(marbles) and marbles[result] == q:
                print('{:d} found at {:d}'.format(q, result + 1))
            else:
                print('{:d} not found'.format(q))

        case += 1


solution()


