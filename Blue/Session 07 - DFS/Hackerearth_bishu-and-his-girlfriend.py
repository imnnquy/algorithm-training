#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/description/


def find_girl(N, graph, girls):
    s = []
    visited = [False for i in range(N + 1)]

    roads = [0 for i in range(N + 1)]

    visited[1] = True
    s.append(1)

    selected_girl = N
    selected_road = N

    while len(s) > 0:
        u = s[-1]
        s.pop()

        for v in graph[u]:
            if not visited[v]:
                roads[v] = roads[u] + 1
                if roads[v] <= selected_road:
                    if girls[v]:
                        if roads[v] < selected_road or (roads[v] == selected_road and selected_girl > v):
                            selected_girl = v
                            selected_road = roads[v]
                            visited[v] = True
                    else:
                        visited[v] = True
                        s.append(v)

    return selected_girl


def solution():
    N = int(input())
    roads = []
    graph = [[] for i in range(N + 1)]
    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    Q = int(input())
    girls = [0 for i in range(N + 1)]
    for i in range(Q):
        girls[int(input())] = 1

    print(find_girl(N, graph, girls))


solution()
