# Problem from Codeforces
# http://codeforces.com/problemset/problem/518/A

# Vitaly is a diligent student who never missed a lesson in his five years of studying in the university. He always does his homework on time and passes his exams in time.
#
# During the last lesson the teacher has provided two strings s and t to Vitaly. The strings have the same length, they consist of lowercase English letters, string s is lexicographically smaller than string t. Vitaly wondered if there is such string that is lexicographically larger than string s and at the same is lexicographically smaller than string t. This string should also consist of lowercase English letters and have the length equal to the lengths of strings s and t.
#
# Let's help Vitaly solve this easy problem!
#
# Input
# The first line contains string s (1 ≤ |s| ≤ 100), consisting of lowercase English letters. Here, |s| denotes the length of the string.
#
# The second line contains string t (|t| = |s|), consisting of lowercase English letters.
#
# It is guaranteed that the lengths of strings s and t are the same and string s is lexicographically less than string t.
#
# Output
# If the string that meets the given requirements doesn't exist, print a single string "No such string" (without the quotes).
#
# If such string exists, print it. If there are multiple valid strings, you may print any of them.
#
# Examples
# input
# a
# c
# output
# b
# input
# aaa
# zzz
# output
# kkk
# input
# abcdefg
# abcdefh
# output
# No such string
# Note
# String s = s1s2... sn is said to be lexicographically smaller than t = t1t2... tn, if there exists such i, that s1 = t1, s2 = t2, ... si - 1 = ti - 1, si < ti.

s = input().strip()
t = input().strip()
first_smaller = -1
result = 'No such string'
for i in range(len(s)):
    if ord(t[i]) - ord(s[i]) >= 2:
        result = s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
        break
    if ord(t[i]) > ord(s[i]):
        first_smaller = i
        break

if first_smaller >= 0:
    if s[first_smaller + 1:] >= t[first_smaller + 1:]:
        for i in range(first_smaller + 1, len(t)):
            if t[i] is not 'a':
                result = s[:first_smaller] + chr(ord(s[first_smaller]) + 1) + t[first_smaller + 1:i] + chr(
                    ord(t[i]) - 1) + t[i + 1:]
                break
            if s[i] is not 'z':
                result = s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
                break
    elif s[first_smaller + 1:] < t[first_smaller + 1:]:
        result = s[:first_smaller] + chr(ord(s[first_smaller]) + 1) + s[first_smaller + 1:]

print(result)


#  New solution: +1 for s
