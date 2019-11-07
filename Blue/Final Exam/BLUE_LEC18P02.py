# BLUE_LEC18P02
import math


def solution():
    T = int(input())

    for i in range(T):
        second = int(input())

        sqrt = math.ceil(math.sqrt(second))
        r = sqrt * sqrt - second
        if r < sqrt:
            y = r + 1
            x = sqrt
        else:
            x = 2 * sqrt - r - 1
            y = sqrt

        if sqrt % 2 == 1:
            x, y = y, x

        print("Case {0}: {1} {2}".format(i + 1, x, y))


solution()
