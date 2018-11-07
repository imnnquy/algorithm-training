# Problem from UVA 10901 - Ferry Loading III
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1842

import queue

n_test_cases = int(input())
results = []
for i in range(n_test_cases):
    n, t, m = map(int, input().split())
    tmp_result = [0] * m
    left_queue = queue.Queue()
    right_queue = queue.Queue()

    for j in range(m):
        ti, side = input().split()
        if side == 'left':
            left_queue.put({'index': j, 'time': int(ti)})
        else:
            right_queue.put({'index': j, 'time': int(ti)})
    current_time = 0
    at_left = True
    while right_queue.qsize() > 0 or left_queue.qsize() > 0:
        if at_left:
            if left_queue.qsize() == 0 or left_queue.queue[0]['time'] > current_time:
                if left_queue.qsize() == 0 or (right_queue.qsize() > 0 and right_queue.queue[0]['time'] < left_queue.queue[0]['time']):
                    current_time = max(right_queue.queue[0]['time'] + t, current_time + t)
                    at_left = not at_left
                    continue
                else:
                    current_time = left_queue.queue[0]['time']
            for k in range(n):
                if left_queue.qsize() > 0 and left_queue.queue[0]['time'] <= current_time:
                    tmp_result[left_queue.queue[0]['index']] = current_time + t
                    left_queue.get()
                else:
                    break
            current_time += t
        else:
            if right_queue.qsize() == 0 or right_queue.queue[0]['time'] > current_time:
                if right_queue.qsize() == 0 or (left_queue.qsize() > 0 and left_queue.queue[0]['time'] < right_queue.queue[0]['time']):
                    current_time = max(left_queue.queue[0]['time'] + t, current_time + t)
                    at_left = not at_left
                    continue
                else:
                    current_time = right_queue.queue[0]['time']
            for k in range(n):
                if right_queue.qsize() > 0 and right_queue.queue[0]['time'] <= current_time:
                    tmp_result[right_queue.queue[0]['index']] = current_time + t
                    right_queue.get()
                else:
                    break
            current_time += t
        at_left = not at_left

    results.append(tmp_result)

for i in range(len(results)):
    print(*results[i], sep='\n')
    if i < len(results) - 1:
        print()
