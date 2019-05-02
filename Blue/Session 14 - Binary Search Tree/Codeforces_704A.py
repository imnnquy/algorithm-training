# Problem from Codeforces
# http://codeforces.com/problemset/problem/704/A
import queue


class Node:
    def __init__(self, noti_index, app_index):
        self.noti_index = noti_index
        self.app_index = app_index

    def __lt__(self, other):
        return self.noti_index < other.noti_index


def solution():
    n, q = map(int, input().strip().split())
    apps = [set() for i in range(n + 1)]
    noti_queue = queue.Queue()
    current_noti = 0
    read_noti = 0
    current_noti_index = 1
    for i in range(q):
        q1, q2 = map(int, input().split())
        if q1 == 1:
            apps[q2].add(current_noti_index)
            noti_queue.put(Node(current_noti_index, q2))
            current_noti_index += 1
            current_noti += 1
        if q1 == 2:
            current_noti -= len(apps[q2])
            apps[q2].clear()
        if q1 == 3:
            while read_noti < q2:
                to_be_read = noti_queue.get()
                if to_be_read.noti_index in apps[to_be_read.app_index]:
                    current_noti -= 1
                    apps[to_be_read.app_index].remove(to_be_read.noti_index)
                read_noti += 1

        print(current_noti)


solution()
