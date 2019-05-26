# Problem from ACM TIMUS
# http://acm.timus.ru/problem.aspx?space=1&num=1585


def solution():
    penguins = {}
    n_penguins = int(input())
    most_numerous_number = 0
    most_numerous_penguin = ''
    for i in range(n_penguins):
        penguin = input().strip()
        if penguins.get(penguin) is None:
            penguins[penguin] = 1
        else:
            penguins[penguin] += 1
        if penguins[penguin] > most_numerous_number:
            most_numerous_number = penguins[penguin]
            most_numerous_penguin = penguin

    print(most_numerous_penguin)


solution()
