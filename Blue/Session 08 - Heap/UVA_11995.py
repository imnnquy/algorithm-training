#  Problem from UVA
#  https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3146


import heapq
import queue
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


def solution():
    while inp.has_next():

        N = int(inp.next())
        my_heap = []
        my_queue = queue.Queue()
        mystack = []
        is_heap = 1
        is_stack = 1
        is_queue = 1
        for i in range(N):
            c_type = int(inp.next())
            x = int(inp.next())
            if is_stack + is_queue + is_heap == 0:
                continue
            if c_type == 1:
                if is_heap == 1:
                    heapq.heappush(my_heap, -x)
                if is_stack == 1:
                    mystack.append(x)
                if is_queue == 1:
                    my_queue.put(x)
            else:
                if is_heap == 1:
                    if len(my_heap) == 0 or -x != heapq.heappop(my_heap):
                        is_heap = 0
                if is_stack == 1:
                    if len(mystack) == 0 or x != mystack[-1]:
                        is_stack = 0
                    else:
                        mystack.pop()
                if is_queue == 1:
                    if my_queue.qsize() == 0 or x != my_queue.queue[0]:
                        is_queue = 0
                    else:
                        my_queue.get()
        if is_heap + is_queue + is_stack > 1:
            print('not sure')
        elif is_heap + is_queue + is_stack == 0:
            print('impossible')
        else:
            if is_stack == 1:
                print('stack')
            if is_queue == 1:
                print('queue')
            if is_heap == 1:
                print('priority queue')


solution()
