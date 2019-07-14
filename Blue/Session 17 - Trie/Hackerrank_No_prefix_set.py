# Problem from Hackerrank
# https://www.hackerrank.com/challenges/no-prefix-set/problem
import sys


class input_tokenizer:
    __tokens = None

    def has_next(self):
        return self.__tokens != [] and self.__tokens != None

    def next(self):
        token = self.__tokens[-1]
        self.__tokens.pop()
        return token

    def __init__(self):
        self.__tokens = sys.stdin.read().split()[::-1]


inp = input_tokenizer()


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
            return False, s

    if len(tmp.child) > 0:
        result = s
        while len(tmp.child) > 0:
            for key in tmp.child:
                result += key
                tmp = tmp.child[key]
                break

        return False, result
    tmp.countWord += 1
    return 'GOOD SET'


def solution():
    root = Node()
    n = int(inp.next())
    duplicated = False
    for i in range(n):
        s = inp.next()
        result = add_word(root, s)
        if not result[0]:
            print('BAD SET')
            print(result[1])
            duplicated = True
            break
    if not duplicated:
        print('GOOD SET')


solution()
