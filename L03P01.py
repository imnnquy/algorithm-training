n = int(input())
result = 1
for counter in range(2, n + 1):
    result = result * counter % 1000003
print(result)
