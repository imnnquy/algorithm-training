n = int(input())
max_apple, max_orange, cur_basket = 0, 0, 0
for i in range(0, n):
    cur_a, cur_o = map(int, input().split())
    if cur_a > max_apple or (cur_a == max_apple and cur_o > max_orange):
        max_apple = cur_a
        max_orange = cur_o
        cur_basket = i
print(cur_basket + 1)
