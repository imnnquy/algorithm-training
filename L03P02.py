preHeight = 0
while True:
    curHeight = int(input())
    if curHeight == 0:
        print('YES')
        break
    elif curHeight < preHeight:
        print('NO')
        break
    else:
        preHeight = curHeight
