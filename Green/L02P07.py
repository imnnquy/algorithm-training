pre, cur = map(int, input().split())
totalUsed = cur - pre


def calc(total_number):
    if total_number <= 50:
        total_money = total_number * 1484
    elif total_number <= 100:
        total_money = 50 * 1484 + (total_number - 50) * 1533
    elif total_number <= 200:
        total_money = 50 * 1484 + 50 * 1533 + (total_number - 100) * 1786
    elif total_number <= 300:
        total_money = 50 * 1484 + 50 * 1533 + 100 * 1786 + (total_number - 200) * 2242
    elif total_number <= 400:
        total_money = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + (total_number - 300) * 2503
    else:
        total_money = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + 100 * 2503 + (total_number - 400) * 2587
    return total_money * 110 / 100


print(int(calc(totalUsed)))
