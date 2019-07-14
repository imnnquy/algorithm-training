# Problem from Hackerrank
# https://www.hackerrank.com/challenges/contacts/problem
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
        tmp.countWord += 1


def find_word(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return 0
        tmp = tmp.child[ch]
    return tmp.countWord


def solution():
    root = Node()
    n = int(inp.next())
    for i in range(n):
        q = inp.next()
        word = inp.next()
        if q == 'add':
            add_word(root, word)
        if q == 'find':
            print(find_word(root, word))


solution()
