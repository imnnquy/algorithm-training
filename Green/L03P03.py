curMax = 0
curMin = 10
while True:
    curMark = int(input())
    if curMax == 10 and curMin == 0 or curMark == -1:
        break
    if curMark < curMin:
        curMin = curMark
    if curMark > curMax:
        curMax = curMark
print(curMax, curMin)
