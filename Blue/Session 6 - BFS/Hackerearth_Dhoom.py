#  Problem from Hackerearth
#  https://www.hackerearth.com/ja/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/description/


import queue


def find_minimum_time(key_value, lock_value, keys):

    if key_value == lock_value:
        return 0

    visited = [False for i in range(100000)]
    path = [-1 for i in range(100000)]
    q = queue.Queue()
    q.put(key_value)

    while not q.empty():
        u = q.get()
        for key in keys:
            new_key = (key * u) % 100000
            if not visited[new_key]:
                visited[new_key] = True
                q.put(new_key)
                path[new_key] = u
                if lock_value == new_key:
                    return get_time(key_value, lock_value, path)

    return -1


def get_time(key_value, lock_value, path):
    total_time = 0
    current_node = lock_value
    while True:
        if key_value == path[current_node]:
            return total_time + 1
        else:
            total_time += 1
            current_node = path[current_node]


def solution():
    key_value, lock_value = map(int, input().split())
    N = int(input())
    keys = list(map(int, input().split()))

    print(find_minimum_time(key_value, lock_value, keys))


solution()
