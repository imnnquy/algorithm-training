class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_node = None


class MyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = self.head_node

    def print_list(self):
        print_node = self.head_node
        while True:
            if print_node.next_node is None:
                print(print_node.data_val, end='')
                break
            else:
                print(print_node.data_val, end=' ')
                print_node = print_node.next_node

    def add_node(self, value=None):
        new_node = Node(value)
        if self.tail_node is not None:
            self.tail_node.next_node = new_node
            self.tail_node = new_node
        else:
            self.head_node = new_node
            self.tail_node = new_node


link_list = MyLinkedList()
x, y, n = map(int, input().split())
link_list.add_node(x)
link_list.add_node(y)
for counter in range(0, n - 2):
    new_val = (x + y) % 1000007
    link_list.add_node(new_val)
    x = y
    y = new_val
link_list.print_list()
