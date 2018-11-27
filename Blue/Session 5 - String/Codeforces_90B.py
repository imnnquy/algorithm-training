# Problem from Codeforces
# http://codeforces.com/problemset/problem/90/B

# An African crossword is a rectangular table n × m in size. Each cell of the table contains exactly one letter. This table (it is also referred to as grid) contains some encrypted word that needs to be decoded.
#
# To solve the crossword you should cross out all repeated letters in rows and columns. In other words, a letter should only be crossed out if and only if the corresponding column or row contains at least one more letter that is exactly the same. Besides, all such letters are crossed out simultaneously.
#
# When all repeated letters have been crossed out, we should write the remaining letters in a string. The letters that occupy a higher position follow before the letters that occupy a lower position. If the letters are located in one row, then the letter to the left goes first. The resulting word is the answer to the problem.
#
# You are suggested to solve an African crossword and print the word encrypted there.
#
# Input
# The first line contains two integers n and m (1 ≤ n, m ≤ 100). Next n lines contain m lowercase Latin letters each. That is the crossword grid.
#
# Output
# Print the encrypted word on a single line. It is guaranteed that the answer consists of at least one letter.
#
# Examples
# input
# 3 3
# cba
# bcd
# cbc
# output
# abcd
# input
# 5 5
# fcofd
# ooedo
# afaoa
# rdcdf
# eofsf
# output
# codeforces


n, m = map(int, input().split())
rectangular = []
result = ''

matrix = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    rectangular.append(input())

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:  # not crossed yet
            for row_checker in range(m):
                if row_checker != j and rectangular[i][row_checker] == rectangular[i][j]:
                    matrix[i][row_checker] = 1
                    matrix[i][j] = 1
            for col_checker in range(n):
                if col_checker != i and rectangular[col_checker][j] == rectangular[i][j]:
                    matrix[col_checker][j] = 1
                    matrix[i][j] = 1


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            result += rectangular[i][j]

print(result)
