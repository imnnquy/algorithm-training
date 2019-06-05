# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1167
# import sys


# sys.stdin = open("file.txt", "r")


def solution():
    n = int(input())
    input()

    for i in range(n):
        population = {}
        total = 0
        while True:
            try:
                new_line = input()
                if not new_line:
                    break
            except:
                break
            if population.get(new_line) is None:
                population[new_line] = 1
            else:
                population[new_line] += 1

            total += 1
        sorted_list = sorted(population.keys())

        for tree in sorted_list:
            print(tree + ' ' + str(round(population.get(tree) * 100 / total, 4)))


solution()
