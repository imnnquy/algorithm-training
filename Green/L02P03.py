inputMonth = int(input())
addQuar = 0 if inputMonth % 3 == 0 else 1
print(inputMonth // 3 + addQuar)
