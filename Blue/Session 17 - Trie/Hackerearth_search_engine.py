# Problem from Hackerearth
# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/


class Node:
    def __init__(self):
        self.maxWeight = 0
        self.child = dict()


def add_word(root, s, weight):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        if tmp.maxWeight < weight:
            tmp.maxWeight = weight


def find_word_max_weight(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return -1
        tmp = tmp.child[ch]
    return tmp.maxWeight


def solution():
    n, q = map(int, input().split())
    root = Node()
    for i in range(n):
        s, weight = map(str, input().strip().split())
        weight = int(weight)
        add_word(root, s, weight)

    for i in range(q):
        word = input().strip()
        print(find_word_max_weight(root, word))


solution()
