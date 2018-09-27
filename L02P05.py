a, b = map(int, input().split())
x = int(input())
if x % a == 0 and x % b == 0:
    result = 'Both'
elif x % a == 0:
    result = 'Upan'
elif x % b == 0:
    result = 'Ipan'
else:
    result = 'No'
print(result)
