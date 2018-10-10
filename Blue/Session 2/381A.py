# http://codeforces.com/contest/381/problem/A

n = int(input())
cards = list(map(int, input().split()))

Sereja = 0
Dima = 0

left = 0
right = n - 1

while True:
    if cards[left] > cards[right]:
        Sereja += cards[left]
        left += 1
    else:
        Sereja += cards[right]
        right -= 1
    if left > right:
        break
    if cards[left] > cards[right]:
        Dima += cards[left]
        left += 1
    else:
        Dima += cards[right]
        right -= 1
    if left > right:
        break

print(Sereja, Dima, sep=' ')
