# Problem from ACM TIMUS
# http://acm.timus.ru/problem.aspx?space=1&num=1196


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
    if root.value < x:
        return search_node(root.right, x)
    return search_node(root.left, x)


def solution():
    n = int(input().strip())

    root = Node(int(input()))
    for i in range(n - 1):
        add_node(root, int(input()))
    m = int(input().strip())
    mark = 0
    for i in range(m):
        year = int(input())
        if search_node(root, year) is not None:
            mark += 1

    print(mark)


solution()
