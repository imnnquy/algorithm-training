inputYear = int(input())
if (inputYear % 4 == 0 and inputYear % 100) != 0 or inputYear % 400 == 0:
    result = 'YES'
else:
    result = 'NO'
print(result)
