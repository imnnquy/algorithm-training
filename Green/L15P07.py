n = int(input())
g_matrix = [list(map(int, input().split())) for i in range(n)]
adjacency_list = [[] for i in range(n)]
edge_counter = 0
for i in range(n):
    for j in range(n):
        if g_matrix[i][j] == 1:
            adjacency_list[i].append(j)
            edge_counter += 1

print(edge_counter)
for i in range(n):
    for j in range(len(adjacency_list[i])):
        print(i, adjacency_list[i][j])
