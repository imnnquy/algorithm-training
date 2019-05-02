# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2283
# import sys


# sys.stdin = open("file.txt", "r")
class Recipe:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        elif self.cost == other.cost:
            return self.name < other.name
        return False


def solution():
    binders = int(input())
    for i in range(binders):
        binder_name = input().strip().upper()
        m, n, b = map(int, input().strip().split())
        ingredients = {}
        for j in range(m):
            ingredient_name, ingredient_price = map(str, input().split())
            ingredients[ingredient_name] = int(ingredient_price)
        print(binder_name)
        can_makes = []
        for j in range(n):
            recipe_name = input().strip()
            k = int(input())
            total_cost = 0
            for x in range(k):
                ingredient_name, quantity = map(str, input().split())
                quantity = int(quantity)
                total_cost += quantity * ingredients[ingredient_name]

            if total_cost <= b:
                can_makes.append(Recipe(recipe_name, total_cost))

        if len(can_makes) == 0:
            print('Too expensive!')
        else:
            can_makes.sort()
            n_can_makes = len(can_makes)
            for cm in range(n_can_makes):
                print(can_makes[cm].name)
        print()


solution()
