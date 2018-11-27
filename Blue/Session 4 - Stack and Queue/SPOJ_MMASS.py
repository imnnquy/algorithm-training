# Problem from SPOJ
# https://www.spoj.com/problems/MMASS/

# MMASS - Mass
# of
# Molecule
# # ad-hoc-1
# English
# Vietnamese
# A molecule can be defined as a sequence of atoms and represented by a chemical formula consisting of letters denoting these atoms. E.g. letter H denotes atom of hydrogen, C denotes atom of carbon, O denotes atom of oxygen, formula COOH represents molecule consisting of one atom of carbon, two atoms of oxygen and one atom of hydrogen.
#
# To write some formulas efficiently, we use the following rules. Letters denoting some atoms can be grouped by enclosing in parentheses, e.g. formula CH(OH) contains group OH. Groups can be nested – a group can also contain other groups. To simplify a formula, consecutive occurrences of the same letter can be replaced with that letter followed by a number of these occurrences. E.g. formula COOHHH can be written as CO2H3 and it represents a molecule consisting of one atom of carbon, two atoms of oxygen and three atoms of hydrogen. Furthermore, consecutive occurrences of the same group can be replaced with that group followed by a number of these occurrences. E.g. formula CH (CO2H) (CO2H) (CO2H) can be written as CH(CO2H)3 and molecule represented by both those formulas consists of four atoms of carbon, four atoms of hydrogen and six atoms of oxygen. A number written after a letter or a group is always greater than or equal to 2 and less than or equal to 9. A mass of a molecule is a sum of masses of all its atoms. One atom of hydrogen has mass 1, one atom of carbon has mass 12 and one atom of oxygen has mass 16.
#
# Write a program that will calculate a mass of a molecule.
#
# Input
# The first and only line of input file contains a formula of a molecule whose mass needs to be determined. A formula of a molecule will consist of characters H, C, O, (, ) , 2, 3, ..., 9 only. Its length will be less or equal to 100 characters.
#
# Output
# The first and only line of output file should contain a mass of a molecule represented with a given formula. The result will always be less than or equal to 10,000.
#
# Sample
# MASS.IN
#
# COOH
#
# MASS.OUT
#
# 45
#
# MASS.IN
#
# CH(CO2H)
# 3
#
# MASS.OUT
#
# 148
#
# MASS.IN
#
# ((CH)2(OH2H)(C(H))O)3
#
# MASS.OUT
#
# 222


def get_value(atom):
    if atom == 'H':
        return 1
    if atom == 'O':
        return 16
    if atom == 'C':
        return 12
    return 0


formula = input().strip()
stack = []
for i in range(len(formula)):
    if formula[i] == '(':
        stack.append(formula[i])
    if formula[i] == ')':
        tmp_total = 0
        while len(stack) > 0:
            if stack[-1] != '(':
                tmp_total += int(stack.pop())
            else:
                stack.pop()
                break
        stack.append(tmp_total)
    if get_value(formula[i]) > 0:
        if len(stack) == 0 or isinstance(stack[-1], int) and i < len(formula) - 1 and not formula[i+1].isdigit():
            if len(stack) > 0:
                stack[-1] = int(stack[-1]) + get_value(formula[i])
            else:
                stack.append(get_value(formula[i]))
        else:
            stack.append(get_value(formula[i]))
    if formula[i].isdigit():
        if isinstance(stack[-1], int):
            stack[-1] = int(stack[-1]) * int(formula[i])
total_result = 0
while len(stack) > 0:
    total_result += int(stack.pop())

print(total_result)
