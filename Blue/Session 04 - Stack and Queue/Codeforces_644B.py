# Problem from Codeforces
# http://codeforces.com/problemset/problem/644/B

# In this problem you have to simulate the workflow of one-thread server. There are n queries to process, the i-th will be received at moment ti and needs to be processed for di units of time. All ti are guaranteed to be distinct.
#
# When a query appears server may react in three possible ways:
#
# If server is free and query queue is empty, then server immediately starts to process this query.
# If server is busy and there are less than b queries in the queue, then new query is added to the end of the queue.
# If server is busy and there are already b queries pending in the queue, then new query is just rejected and will never be processed.
# As soon as server finished to process some query, it picks new one from the queue (if it's not empty, of course). If a new query comes at some moment x, and the server finishes to process another query at exactly the same moment, we consider that first query is picked from the queue and only then new query appears.
#
# For each query find the moment when the server will finish to process it or print -1 if this query will be rejected.
#
# Input
# The first line of the input contains two integers n and b (1 ≤ n, b ≤ 200 000) — the number of queries and the maximum possible size of the query queue.
#
# Then follow n lines with queries descriptions (in chronological order). Each description consists of two integers ti and di (1 ≤ ti, di ≤ 109), where ti is the moment of time when the i-th query appears and di is the time server needs to process it. It is guaranteed that ti - 1 < ti for all i > 1.
#
# Output
# Print the sequence of n integers e1, e2, ..., en, where ei is the moment the server will finish to process the i-th query (queries are numbered in the order they appear in the input) or  - 1 if the corresponding query will be rejected.
#
# Examples
# input
# 5 1
# 2 9
# 4 8
# 10 9
# 15 2
# 19 1
# output
# 11 19 -1 21 22
# input
# 4 1
# 2 8
# 4 8
# 10 9
# 15 2
# output
# 10 18 27 -1
# Note
# Consider the first sample.
#
# The server will start to process first query at the moment 2 and will finish to process it at the moment 11.
# At the moment 4 second query appears and proceeds to the queue.
# At the moment 10 third query appears. However, the server is still busy with query 1, b = 1 and there is already query 2 pending in the queue, so third query is just rejected.
# At the moment 11 server will finish to process first query and will take the second query from the queue.
# At the moment 15 fourth query appears. As the server is currently busy it proceeds to the queue.
# At the moment 19 two events occur simultaneously: server finishes to proceed the second query and the fifth query appears. As was said in the statement above, first server will finish to process the second query, then it will pick the fourth query from the queue and only then will the fifth query appear. As the queue is empty fifth query is proceed there.
# Server finishes to process query number 4 at the moment 21. Query number 5 is picked from the queue.
# Server finishes to process query number 5 at the moment 22.

import queue

n, b = map(int, input().split())
result = [0] * n
last_processing = 0
waiting_queue = queue.Queue()
for i in range(n):
    ti, di = map(int, input().split())
    while waiting_queue.qsize() > 0 and last_processing <= ti:
        last_processing = max(last_processing, waiting_queue.queue[0]['time']) + waiting_queue.queue[0]['take_time']
        result[waiting_queue.queue[0]['index']] = last_processing
        waiting_queue.get()
    if waiting_queue.qsize() < b:
        waiting_queue.put({'index': i, 'time': ti, 'take_time': di})
    else:
        result[i] = -1

while waiting_queue.qsize() > 0:
    last_processing = max(last_processing, waiting_queue.queue[0]['time']) + waiting_queue.queue[0]['take_time']
    result[waiting_queue.queue[0]['index']] = last_processing
    waiting_queue.get()
print(*result, sep=' ')
