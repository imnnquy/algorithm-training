# Problem from LightOJ
# http://lightoj.com/volume_showproblem.php?problem=1129


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
    tmp.countWord += 1
    return True


def solution():
    T = int(input())
    for t in range(T):
        root = Node()
        n = int(input())
        duplicated = False
        for i in range(n):
            s = input().strip()
            if not add_word(root, s):
                print('Case {}: NO'.format(t + 1))
                duplicated = True
                break
        if not duplicated:
            print('Case {}: YES'.format(t + 1))


solution()
