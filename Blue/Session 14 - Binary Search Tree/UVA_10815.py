# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1756
# import sys
import re

# sys.stdin = open("file.txt", "r")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add_node(root, x):
    if root is None:
        return Node(x)
    if x < root.value:
        root.left = add_node(root.left, x)
    elif x > root.value:
        root.right = add_node(root.right, x)
    return root


def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.value)
    print_tree(root.right)


def solution():
    root = None
    while True:
        new_line = None
        new_words = []
        try:
            new_line = input().strip()
            new_words = list(map(lambda word: re.sub('[^a-z]+', '', word.lower()), re.compile(r'[^A-Za-z]').split(new_line)))
        except Exception:
            break

        new_words = list(filter(lambda x: x is not '', new_words))

        if root is None:
            if len(new_words) > 0:
                root = Node(new_words[0])

        for word in new_words:
            add_node(root, word)

    print_tree(root)


solution()

