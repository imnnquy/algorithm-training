# Problem from Codeforces
# http://codeforces.com/problemset/problem/334/B
#
# Gerald is very particular to eight point sets. He thinks that any decent eight point set must consist of all pairwise intersections of three distinct integer vertical straight lines and three distinct integer horizontal straight lines, except for the average of these nine points. In other words, there must be three integers x1, x2, x3 and three more integers y1, y2, y3, such that x1 < x2 < x3, y1 < y2 < y3 and the eight point set consists of all points (xi, yj) (1 ≤ i, j ≤ 3), except for point (x2, y2).
#
# You have a set of eight points. Find out if Gerald can use this set?
#
# Input
# The input consists of eight lines, the i-th line contains two space-separated integers xi and yi (0 ≤ xi, yi ≤ 106). You do not have any other conditions for these points.
#
# Output
# In a single line print word "respectable", if the given set of points corresponds to Gerald's decency rules, and "ugly" otherwise.
#
# Examples
# input
# 0 0
# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1
# 2 2
# output
# respectable
# input
# 0 0
# 1 0
# 2 0
# 3 0
# 4 0
# 5 0
# 6 0
# 7 0
# output
# ugly
# input
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# output
# ugly

