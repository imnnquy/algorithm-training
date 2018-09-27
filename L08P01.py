def calc(km: int) -> int:
    total = 0
    if km <= 1:
        return 15000
    if km > 1 and km <= 5:
        return 15000 + 13500 * (km - 1)
    if km >= 6:
        total = 15000 + 4 * 13500 + (km - 5) * 11000
    if km >= 12:
        total = 90 * total / 100
    return total


inputKm = int(input())
print(int(calc(inputKm)))
