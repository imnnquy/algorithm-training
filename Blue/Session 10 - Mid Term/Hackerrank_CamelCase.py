#  Problem from Hackerrank
#  https://www.hackerrank.com/challenges/camelcase/problem


def solution():

    s = input().strip()
    counter = 1
    for c in s:
        if ord(c) < 97:
            counter += 1

    print(counter)


solution()
