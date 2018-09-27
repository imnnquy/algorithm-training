n = int(input())
edge_list = [list(map(int, input().split())) for i in range(n)]
current_min_weight = 1000
min_wight_counter = 0
for i in range(n):
    if edge_list[i][2] < current_min_weight:
        current_min_weight = edge_list[i][2]
        min_wight_counter = 1
    elif edge_list[i][2] == current_min_weight:
        min_wight_counter += 1
print(current_min_weight * min_wight_counter)
