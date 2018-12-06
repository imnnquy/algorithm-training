#  Problem from Hackerrank
#  https://www.hackerrank.com/challenges/qheap1/problem


import heapq


def solution():
    Q = int(input())
    my_list = []
    delete_list = []
    for i in range(Q):
        query = input()
        if query.startswith('3'):
            while True:
                delete_list_length = len(delete_list)
                contain_in_delete = False
                for j in range(delete_list_length):
                    if my_list[0] == delete_list[j]:
                        heapq.heappop(my_list)
                        delete_list[j] = delete_list[-1]
                        delete_list.pop()
                        contain_in_delete = True
                        break
                if not contain_in_delete:
                    break

            print(my_list[0])
        else:
            command, param = map(int, query.split())
            if command == 1:
                heapq.heappush(my_list, param)
            else:
                delete_list.append(param)


solution()

