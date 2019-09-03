# Problem from UVA 12207	That is Your Queue
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3359

# Your government has finally solved the
# problem of universal health care! Now
# everyone, rich or poor, will finally have
# access to the same level of medical care.
# Hurrah!
# There’s one minor complication. All
# of the country’s hospitals have been condensed
# down into one location, which can
# only take care of one person at a time.
# But don’t worry! There is also a plan
# in place for a fair, efficient computerized
# system to determine who will be admitted.
# You are in charge of programming
# this system.
# Every citizen in the nation will be assigned
# a unique number, from 1 to P
# (where P is the current population). They will be put into a queue, with 1 in front of 2, 2 in front of
# 3, and so on. The hospital will process patients one by one, in order, from this queue. Once a citizen
# has been admitted, they will immediately move from the front of the queue to the back.
# Of course, sometimes emergencies arise; if you’ve just been run over by a steamroller, you can’t wait
# for half the country to get a routine checkup before you can be treated! So, for these (hopefully rare)
# occasions, an expedite command can be given to move one person to the front of the queue. Everyone
# else’s relative order will remain unchanged.
# Given the sequence of processing and expediting commands, output the order in which citizens will
# be admitted to the hospital.

# Input
# Input consists of at most ten test cases. Each test case starts with a line containing P, the population
# of your country (1 ≤ P ≤ 1000000000), and C, the number of commands to process (1 ≤ C ≤ 1000).
# The next C lines each contain a command of the form ‘N’, indicating the next citizen is to be
# admitted, or ‘E x’, indicating that citizen x is to be expedited to the front of the queue.
# The last test case is followed by a line containing two zeros.
# Output
# For each test case print the serial of output. This is followed by one line of output for each ‘N’ command,
# indicating which citizen should be processed next. Look at the output for sample input for details.
# Sample Input
# 3 6
# N
# N
# E 1
# N
# N
# N
# 10 2
# N
# N
# 0 0

# Sample Output
# Case 1:
# 1
# 2
# 1
# 3
# 2
# Case 2:
# 1
# 2


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
        print('---')

    def add_node(self, value=None):
        new_node = Node(value)
        if self.tail_node is not None:
            self.tail_node.next_node = new_node
            self.tail_node = new_node
        else:
            self.head_node = new_node
            self.tail_node = new_node

    def remove_head(self):
        head_value = self.head_node.data_val
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
        else:
            self.head_node = self.head_node.next_node
        return head_value

    def remove_node(self, val_to_remove):
        cur_node = self.head_node
        cur_pre_node = None
        while True:
            if cur_node is None:
                return
            if cur_node.data_val == val_to_remove:
                if cur_pre_node is not None:
                    cur_pre_node.next_node = cur_node.next_node
                else:
                    self.head_node = cur_node.next_node
                if cur_node.next_node is None:
                    self.tail_node = cur_pre_node
                return
            else:
                cur_pre_node = cur_node
                cur_node = cur_node.next_node

    def add_head(self, val_to_add):
        new_node = Node(val_to_add)
        if self.head_node is not None:
            new_node.next_node = self.head_node
            self.head_node = new_node
        else:
            self.head_node = new_node
            self.tail_node = new_node


results = []
while True:
    P, C = map(int, input().split())

    if P == 0:
        break
    P = min(P, C)

    cur_queue = MyLinkedList()
    for i in range(P):
        cur_queue.add_node(i + 1)
    cur_result = []
    for i in range(C):
        Ci = input()
        if Ci is 'N':
            cur_treating = cur_queue.remove_head()
            cur_result.append(cur_treating)
            cur_queue.add_node(cur_treating)
        else:
            expedited_index = int(Ci.split()[1])
            cur_queue.remove_node(expedited_index)
            cur_queue.add_head(expedited_index)

    results.append(cur_result)

for i in range(len(results)):
    print('Case %d:' %(i + 1))
    print(*results[i], sep='\n')
