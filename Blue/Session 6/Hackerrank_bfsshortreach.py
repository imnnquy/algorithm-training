#  Problem from Hackerrank
#  https://www.hackerrank.com/challenges/bfsshortreach/problem


# !/bin/python3

import math
import os
import random
import re
import sys
import queue


# Complete the bfs function below.


def bfs(n, m, edges, s):
    MAX = n + 9
    visited = [False for i in range(MAX)]
    path = [-1 for i in range(MAX)]
    for i in range(1, n + 1):
        visited[i] = False

    graph = [[] for i in range(MAX)]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u

    _result = []
    for i in range(1, n + 1):
        if i != s:
            _result.append(calc_path(s, i, path))

    return _result


def calc_path(s, f, path):
    steps = 0
    if path[f] == -1:
        return -1

    while True:
        steps += 1
        f = path[f]
        if f == s:
            break
    return steps * 6


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
