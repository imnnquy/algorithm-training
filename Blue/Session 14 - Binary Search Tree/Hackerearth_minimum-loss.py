#  Problem from Hackerearth
#  https://www.hackerrank.com/contests/womens-codesprint-2/challenges/minimum-loss


#!/bin/python3

import math
import os
import random
import re
import sys


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


def search_node(root, x):
    if root is None or root.value == x:
        return root
    if root.key < x:
        return search_node(root.right, x)
    return search_node(root.left, x)


def max_value_node(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.value


def __find_min_loss(root):
    if root is None or root.left is None:
        return -1
    return root.value - max_value_node(root.left)


def find_min_loss(root, min_loss):
    if root is None:
        return min_loss
    current_min_loss = __find_min_loss(root)
    if current_min_loss != -1 and min_loss > current_min_loss:
        min_loss = current_min_loss

    min_loss_right = find_min_loss(root.right, min_loss)
    min_loss_left = find_min_loss(root.left, min_loss)

    return min(min_loss_left, min_loss_right)


# Complete the minimumLoss function below.
def minimum_loss(price):
    n = len(price)
    root = Node(price[0])
    for i in range(1, n):
        add_node(root, price[i])

    min_loss = 1e16
    return find_min_loss(root, min_loss)


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimum_loss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

