# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1415
# import sys
import bisect

INF = float(1e9)
# sys.stdout = open("file.txt", "w+")


class Marble:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value


def solution():
    case = 1
    while True:
        N, Q = map(int, input().strip().split())

        if N == 0:
            break

        marbles = []
        for i in range(N):
            marbles.append(Marble(int(input().strip()), i + 1))

        # sorted(marbles)
        marbles.sort()

        print('CASE# ' + str(case) + ':')
        for i in range(Q):
            q = int(input().strip())
            result = bisect.bisect_left(marbles, Marble(q, 0))

            if marbles[result] == Marble(q, 0):
                print('{:d} found at {:d}'.format(q, result + 1))
            else:
                print('{:d} not found'.format(q))


solution()


