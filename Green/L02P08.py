m, n, a = map(int, input().split())
addM = 0 if m % a == 0 else 1
addN = 0 if n % a == 0 else 1
result = (m // a + addM) * (n // a + addN)
print(result)
