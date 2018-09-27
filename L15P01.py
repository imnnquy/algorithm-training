class Edge:
    def __init__(self, n_from, n_to):
        self.n_from = n_from
        self.n_to = n_to

    def print_node(self):
        print(self.n_from, self.n_to)


n = int(input())
g_matrix = [list(map(int, input().split())) for i in range(n)]
edge_list = []
for i in range(n):
    for j in range(i, n):
        if g_matrix[i][j] > 0:
            edge_list.append(Edge(i, j))
print(len(edge_list))
for edge in edge_list:
    edge.print_node()
