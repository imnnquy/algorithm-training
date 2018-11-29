# Problem from URI
# https://www.urionlinejudge.com.br/judge/en/problems/view/1610


def sim_nao(N, graph):
    global_visited = [False for i in range(N+1)]

    for i in range(1, N + 1):
        if not global_visited[i]:
            visited = [False for i in range(N + 1)]
            s = [i]
            global_visited[i] = True
            visited[i] = True
            while len(s) > 0:
                u = s[-1]
                s.pop()
                for v in graph[u]:
                    if not visited[v]:
                        s.append(v)
                        visited[v] = True
                        global_visited[u] = True
                    else:
                        return 'SIM'

    return 'NAO'


def solution():
    results = []
    T = int(input())
    for i in range(T):

        while True:
            new_line = input().strip()
            if new_line:
                N, M = map(int, new_line.split())
                break

        graph = [[] for i in range(N + 1)]
        for j in range(M):
            while True:
                new_line = input().strip()
                if new_line:
                    A, B = map(int, new_line.split())
                    if not B in graph[A]:
                        graph[A].append(B)
                    break
        results.append(sim_nao(N, graph))

    print(*results, sep='\n')


solution()


