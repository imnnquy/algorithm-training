# Problem from icpcarchive
# https://icpcarchive.ecs.baylor.edu/index.php?option=onlinejudge&page=show_problem&problem=3803
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
        return False
    tmp.countWord += 1
    return True


def solution():

    while True:
        P = int(inp.next())
        S = int(inp.next())
        P_words = []
        S_words = []
        root = Node()
        if P == 0 and S == 0:
            break
        for i in range(P):
            P_words.append(inp.next())

        for i in range(S):
            S_words.append(inp.next())

        total = 0
        for i in range(P):
            p_len = len(P_words[i])
            for k in range(1, p_len + 1):
                for j in range(S):
                    s_len = len(S_words[j])
                    for l in range(s_len):
                        new_word = P_words[i][:k] + S_words[j][l:s_len]
                        if add_word(root, new_word):
                            total += 1
        print(total)


solution()
