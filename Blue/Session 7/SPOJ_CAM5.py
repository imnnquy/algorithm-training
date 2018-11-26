#  Problem from SPOJ
#  https://www.spoj.com/problems/CAM5/


def calc_disjoint_sets(Ni, graph):
    result = 0
    visited = [False for i in range(Ni)]

    for i in range(Ni):
        if visited[i]:
            continue
        stack = [i]
        visited[i] = True

        while len(stack) > 0:
            u = stack[-1]
            stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        result += 1

    return result


def solution():
    results = []
    while True:
        new_line = input().strip()
        if new_line:
            t = int(new_line)
            break
    for i in range(t):
        while True:
            new_line = input().strip()
            if new_line:
                Ni = int(new_line)
                break
        ei = int(input())
        graph = [[] for jj in range(Ni)]
        for j in range(ei):
            start, end = map(int, input().split())
            graph[start].append(end)
            graph[end].append(start)

        results.append(calc_disjoint_sets(Ni, graph))

    print(*results, sep='\n')


solution()
