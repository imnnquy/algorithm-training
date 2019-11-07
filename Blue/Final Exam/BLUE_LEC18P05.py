# BLUE_LEC18P0o4


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def add_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        if tmp.countWord > 0:
            return False

    if len(tmp.child) > 0:
        return False
    tmp.countWord += 1
    return True


def solution():
    tc = int(input())
    for t in range(tc):
        root = Node()
        n = int(input())
        duplicated = False
        for i in range(n):
            s = input()
            result = add_word(root, s)
            if not result:
                print('NO')
                duplicated = True
                break
        if not duplicated:
            print('YES')


solution()
