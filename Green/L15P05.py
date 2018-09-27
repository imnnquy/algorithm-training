n = int(input())
edge_list = [list(map(int, input().split())) for i in range(n)]
number_of_loops = 0
mult_loops = 1
for i in range(n):
    if edge_list[i][0] == edge_list[i][1]:
        number_of_loops += 1
        mult_loops *= edge_list[i][2]
print(number_of_loops, end=' ')
print(mult_loops if number_of_loops > 0 else -1)
