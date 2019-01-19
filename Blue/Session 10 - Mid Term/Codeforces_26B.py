# Problem from Codeforces
# http://codeforces.com/problemset/problem/26/B


def solution():
    s = input().strip()
    pos = 0
    total = 0
    for c in s:
        if c == '(':
            pos += 1
        else:
            pos -= 1
            if pos >= 0:
                total += 2
            else:
                pos += 1

    print(total)


solution()


