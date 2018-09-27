def check_jacket(_a, _n):
    un_fastened = 0
    if _n == 1:
        if _a[0] == 0:
            return 'NO'
        else:
            return 'YES'
    else:
        for i in range(_n):
            un_fastened += (1 - _a[i])
            if un_fastened > 1:
                return 'NO'
        if un_fastened == 0:
            return 'NO'
        else:
            return 'YES'


n = int(input())
a = list(map(int, input().split()))
print(check_jacket(a, n))


