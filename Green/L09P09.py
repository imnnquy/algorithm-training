def gcd(_a, _b):
    if _b == 0:
        return _a
    else:
        return gcd(_b, _a % _b)


a, b = map(int, input().split())
print(gcd(a, b))
