# Problem from Codeforces
# http://codeforces.com/problemset/problem/6/C

n = int(input())
t = list(map(int, input().split()))

alice_eating_index = 0
bob_eating_index = n - 1
while True:
    if alice_eating_index >= bob_eating_index - 1:
        break
    if t[alice_eating_index] > t[bob_eating_index]:
        t[alice_eating_index] -= t[bob_eating_index]
        bob_eating_index -= 1
    elif t[alice_eating_index] < t[bob_eating_index]:
        t[bob_eating_index] -= t[alice_eating_index]
        alice_eating_index += 1
    else:
        if bob_eating_index - alice_eating_index == 2:
            alice_eating_index += 1
        else:
            alice_eating_index += 1
            bob_eating_index -= 1


print(alice_eating_index + 1, n - alice_eating_index - 1)
