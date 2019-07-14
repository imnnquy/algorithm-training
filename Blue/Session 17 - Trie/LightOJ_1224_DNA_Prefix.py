# Problem from LightOJ
# http://lightoj.com/volume_showproblem.php?problem=1224


class Node:
    def __init__(self):
        self.maxWeight = 0
        self.child = dict()


def add_word(root, s):
    tmp = root
    i = 1
    max_weight = 0
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        tmp.maxWeight += i
        i += 1
        if tmp.maxWeight > max_weight:
            max_weight = tmp.maxWeight
    return max_weight


def find_word_max_weight(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return -1
        tmp = tmp.child[ch]
    return tmp.maxWeight


def solution():
    T = int(input())
    for t in range(T):
        n = int(input())
        root = Node()
        max_weight = 0
        for i in range(n):
            s = input()
            current_max_weight = add_word(root, s)
            if max_weight < current_max_weight:
                max_weight = current_max_weight

        print('Case {}: {}'.format(t + 1, max_weight))


solution()
