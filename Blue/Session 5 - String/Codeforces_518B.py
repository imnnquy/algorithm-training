# Problem from Codeforces
# http://codeforces.com/problemset/problem/518/B

# Little Tanya decided to present her dad a postcard on his Birthday. She has already created a message — string s of length n, consisting of uppercase and lowercase English letters. Tanya can't write yet, so she found a newspaper and decided to cut out the letters and glue them into the postcard to achieve string s. The newspaper contains string t, consisting of uppercase and lowercase English letters. We know that the length of string t greater or equal to the length of the string s.
#
# The newspaper may possibly have too few of some letters needed to make the text and too many of some other letters. That's why Tanya wants to cut some n letters out of the newspaper and make a message of length exactly n, so that it looked as much as possible like s. If the letter in some position has correct value and correct letter case (in the string s and in the string that Tanya will make), then she shouts joyfully "YAY!", and if the letter in the given position has only the correct value but it is in the wrong case, then the girl says "WHOOPS".
#
# Tanya wants to make such message that lets her shout "YAY!" as much as possible. If there are multiple ways to do this, then her second priority is to maximize the number of times she says "WHOOPS". Your task is to help Tanya make the message.
#
# Input
# The first line contains line s (1 ≤ |s| ≤ 2·105), consisting of uppercase and lowercase English letters — the text of Tanya's message.
#
# The second line contains line t (|s| ≤ |t| ≤ 2·105), consisting of uppercase and lowercase English letters — the text written in the newspaper.
#
# Here |a| means the length of the string a.
#
# Output
# Print two integers separated by a space:
#
# the first number is the number of times Tanya shouts "YAY!" while making the message,
# the second number is the number of times Tanya says "WHOOPS" while making the message.
# Examples
# input
# AbC
# DCbA
# output
# 3 0
# input
# ABC
# abc
# output
# 0 3
# input
# abacaba
# AbaCaBA
# output
# 3 4

s = input().strip()
t = input().strip()

yay = 0
whoops = 0

yay_map = [0] * 58
whoops_map = [] * 58

slength = len(s)
tlength = len(t)

s_map = [0] * 58
t_map = [0] * 58
up_low_distance = 32

for i in range(slength):
    s_map[ord(s[i]) - 65] += 1

for i in range(tlength):
    t_map[ord(t[i]) - 65] += 1

for i in range(26):
    # Go with YAY!
    if t_map[i] >= s_map[i]:
        yay += s_map[i]
        t_map[i] -= s_map[i]
        s_map[i] = 0
    else:
        yay += t_map[i]
        s_map[i] -= t_map[i]
        t_map[i] = 0

    if t_map[i + up_low_distance] >= s_map[i + up_low_distance]:
        yay += s_map[i + up_low_distance]
        t_map[i + up_low_distance] -= s_map[i + up_low_distance]
        s_map[i + up_low_distance] = 0
    else:
        yay += t_map[i + up_low_distance]
        s_map[i + up_low_distance] -= t_map[i + up_low_distance]
        t_map[i + up_low_distance] = 0

    # Go with WHOOPS
    if t_map[i] >= s_map[i + up_low_distance]:
        whoops += s_map[i + up_low_distance]
        t_map[i] -= s_map[i + up_low_distance]
        s_map[i + up_low_distance] = 0
    else:
        whoops += t_map[i]
        s_map[i + up_low_distance] -= t_map[i]
        t_map[i] = 0

    if t_map[i + up_low_distance] >= s_map[i]:
        whoops += s_map[i]
        t_map[i + up_low_distance] -= s_map[i]
        s_map[i] = 0
    else:
        whoops += t_map[i + up_low_distance]
        s_map[i] -= t_map[i + up_low_distance]
        t_map[i + up_low_distance] = 0

print(yay, whoops)
