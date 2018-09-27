def check_symmetry(n):
    n_str = str(n)
    n_length = len(n_str)
    range_counter = n_length // 2
    for counter in range(0, range_counter):
        if n_str[counter] != n_str[-counter-1]:
            return 'NO'
    return 'YES'


n = int(input())
print(check_symmetry(n))
