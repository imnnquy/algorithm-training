# Compilers and parsers Problem Code: COMPILER
# https://www.codechef.com/problems/COMPILER

# Lira is now very keen on compiler development. :)
#
# She knows that one of the most important components of a compiler, is its parser.
#
#     A parser is, in simple terms, a software component that processes text, and checks it's semantic correctness, or, if you prefer, if the text is properly built.
#
# As an example, in declaring and initializing an integer, in C/C++, you can't do something like:
#
# int = x ;4
#
# as the semantics of such statement is incorrect, as we all know that the datatype must precede an identifier and only afterwards should come the equal sign and the initialization value, so, the corrected statement should be:
#
# int x = 4;
#
# Today, Lira is concerned with an abstract instruction which is composed of the characters "<" and ">" , which she will use on the design of her language, L++ :D.
#
#                                                                                                                                                                    She is using it as an abstraction for generating XML code Tags in an easier fashion and she understood that, for an expression to be valid, a "<" symbol must always have a corresponding ">" character somewhere (not necessary immediately) after it. Moreover, each ">" symbol should correspond to exactly one "<" symbol.
#
# So, for instance, the instructions:
#
#     <<>>
#
# <>
#
# <><>
#
# are all valid. While:
#
# >>
#
# ><><
#
# are not.
#
# Given some expressions which represent some instructions to be analyzed by Lira's compiler, you should tell the length of the longest prefix of each of these expressions that is valid, or 0 if there's no such a prefix.
#
#     Input
# Input will consist of an integer T denoting the number of test cases to follow.
#
#                                                                             Then, T strings follow, each on a single line, representing a possible expression in L++.
#
# Output
# For each expression you should output the length of the longest prefix that is valid or 0 if there's no such a prefix.
# Constraints
# 1 ≤ T ≤ 500
# 1 ≤ The length of a single expression ≤ 106
# The total size all the input expressions is no more than 5*106
#
#
# Example
# Input:
# 3
# <<>>
# ><
# <>>>
# Output:
# 4
# 0
# 2


T = int(input())

results = []
for i in range(T):
    cur_exp = input().strip()
    my_stack = []
    exp_length = len(cur_exp)
    cur_result = 0
    cur_max = 0
    for j in range(exp_length):
        if cur_exp[j] == '>':
            if len(my_stack) == 0:
                break
            else:
                my_stack.pop()
                cur_result += 1
                if len(my_stack) == 0:
                    cur_max = cur_result
        if cur_exp[j] == '<':
            my_stack.append('<')
            cur_result += 1
    results.append(cur_max)

print(*results, sep='\n')
