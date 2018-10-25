# Problem from Codeforces
# http://codeforces.com/problemset/problem/37/A

# Little Vasya has received a young builder’s kit. The kit consists of several wooden bars, the lengths of all of them are known. The bars can be put one on the top of the other if their lengths are the same.
#
# Vasya wants to construct the minimal number of towers from the bars. Help Vasya to use the bars in the best way possible.
#
# Input
# The first line contains an integer N (1 ≤ N ≤ 1000) — the number of bars at Vasya’s disposal. The second line contains N space-separated integers li — the lengths of the bars. All the lengths are natural numbers not exceeding 1000.
#
# Output
# In one line output two numbers — the height of the largest tower and their total number. Remember that Vasya should use all the bars.
#
# Examples
# input
# 3
# 1 2 3
# output
# 1 3
# input
# 4
# 6 5 6 7
# output
# 2 3

n = int(input())
L = list(map(int, input().split()))
L.sort()

number_of_towers = 1
highest_tower = 1
current_tower_height = 1

for i in range(1, n):
    if L[i] == L[i - 1]:
        current_tower_height += 1
        if current_tower_height > highest_tower:
            highest_tower = current_tower_height
    else:
        number_of_towers += 1
        current_tower_height = 1

print(highest_tower, number_of_towers, sep=' ')
