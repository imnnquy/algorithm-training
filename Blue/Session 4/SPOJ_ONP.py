# Problem from SPOJ
# https://www.spoj.com/problems/ONP/

# ONP - Transform the Expression
# #stack
# Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).
#
# Input
# t [the number of expressions <= 100]
# expression [length <= 400]
# [other expressions]
# Text grouped in [ ] does not appear in the input file.
#
# Output
# The expressions in RPN form, one per line.
# Example
# Input:
# 3
# (a+(b*c))
# ((a+b)*(z+x))
# ((a+t)*((b+(a+c))^(c+d)))
#
# Output:
# abc*+
# ab+zx+*
# at+bac++cd+^*

n = int(input())
results = []

operator_list = {
    '+': 1,
    '-': 2,
    '*': 3,
    '/': 4,
    '^': 5
}

for i in range(n):
    cur_exp = input()
    cur_length = len(cur_exp)
    cur_output = ''
    temp_stack = []
    for j in range(cur_length):
        cur_elem = cur_exp[j]
        cur_prio = operator_list.get(cur_elem)
        if cur_prio is None and cur_elem is not ')' and cur_elem is not '(': # This is a number
            cur_output += cur_elem
        elif cur_prio is not None: # This is an operator
            if len(temp_stack) > 0 and operator_list.get(temp_stack[-1]) is not None and operator_list.get(temp_stack[-1]) >= cur_prio:
                cur_output += temp_stack.pop()
            temp_stack.append(cur_elem)
        elif cur_elem is '(':
            temp_stack.append(cur_elem)
        else:
            while len(temp_stack) > 0:
                fr_stack = temp_stack.pop()
                if fr_stack is '(':
                    break
                cur_output += fr_stack

    while len(temp_stack) > 0:
        fr_stack = temp_stack.pop()
        cur_output += fr_stack

    results.append(cur_output)

print(*results, sep='\n')
