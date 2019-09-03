# Problem from SPOJ
# https://www.spoj.com/problems/STPAR/

# For sure, the love mobiles will roll again on this summer's street parade. Each year, the organisers decide on a fixed order for the decorated trucks. Experience taught them to keep free a side street to be able to bring the trucks into order.
#
# The side street is so narrow that no two cars can pass each other. Thus, the love mobile that enters the side street last must necessarily leave the side street first. Because the trucks and the ravers move up closely, a truck cannot drive back and re-enter the side street or the approach street.
#
# You are given the order in which the love mobiles arrive. Write a program that decides if the love mobiles can be brought into the order that the organisers want them to be.
#
# Input
# There are several test cases. The first line of each test case contains a single number n, the number of love mobiles. The second line contains the numbers 1 to n in an arbitrary order. All the numbers are separated by single spaces. These numbers indicate the order in which the trucks arrive in the approach street. No more than 1000 love mobiles participate in the street parade. Input ends with number 0.
#
# Output
# For each test case your program has to output a line containing a single word "yes" if the love mobiles can be re-ordered with the help of the side street, and a single word "no" in the opposite case.
#
# Example
# Sample input:
# 5
# 5 1 2 4 3
# 0
#
# Sample output:
# yes

results = []
while True:
    n = int(input())
    if n == 0:
        break

    trucks = list(map(int, input().split()))

    side_street = []
    result_order = []

    current_expect = 1

    while True:
        if len(trucks) > 0:
            if trucks[0] == current_expect:
                current_expect += 1
                result_order.append(trucks.pop(0))
            elif len(side_street) > 0 and side_street[-1] == current_expect:
                result_order.append(side_street.pop())
                current_expect += 1
            else:
                side_street.append(trucks.pop(0))
        elif len(side_street) > 0:
            from_side_street = side_street.pop()
            if from_side_street == current_expect:
                result_order.append(from_side_street)
                current_expect += 1
            else:
                results.append('no')
                break
        else:
            results.append('yes')
            break
print(*results, sep='\n')
