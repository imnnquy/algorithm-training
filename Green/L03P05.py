import math


def is_prime(n_to_check):
    if n == 1:
        return 'NO'
    upper_range = math.sqrt(n_to_check)
    for counter in range(2, int(upper_range) + 1):
        if n_to_check % counter == 0:
            return 'NO'
    return 'YES'


n = int(input())
print(is_prime(n))
