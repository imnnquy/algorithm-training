def fibo(n: int) -> int:
    if n < 2:
        return 1
    if n == 2:
        return 2
    a = [0] * (n + 2)
    a[0] = a[1] = 1
    for counter in range(2, n + 1):
        a[counter] = a[counter - 1] + a[counter - 2]
    return a[n]


n, m = map(int, input().split())
print(fibo(n - 1) % m)
