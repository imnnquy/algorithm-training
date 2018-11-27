# Problem from URI
# https://www.urionlinejudge.com.br/judge/en/problems/view/1610


def sim_nao(N, M, graph):
    visited = [0 for i in range(N + 1)]
    current_max_visit = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            s = [i]
            visited[i] = current_max_visit + 1
            current_max_visit = visited[i]
            while len(s) > 0:
                u = s[-1]
                s.pop()
                for v in graph[u]:
                    if visited[v] == 0:
                        s.append(v)
                        visited[v] = current_max_visit
                    elif visited[v] < current_max_visit:
                        continue
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
        results.append(sim_nao(N, M, graph))

    print(*results, sep='\n')


solution()


