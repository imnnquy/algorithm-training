#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    current_hori_right_obs = None
    current_hori_left_obs = None

    current_vert_up_obs = None
    current_vert_down_obs = None

    current_front_up_obs = None
    current_front_down_obs = None

    current_back_up_obs = None
    current_back_down_obs = None

    for i in range(k):
        if obstacles[i][0] == r_q:  # same row
            if obstacles[i][1] > c_q:  # check hori right
                if current_hori_right_obs is None or current_hori_right_obs[1] > obstacles[i][1]:
                    current_hori_right_obs = obstacles[i]
            if obstacles[i][1] < c_q:  # check hori left
                if current_hori_left_obs is None or current_hori_left_obs[1] < obstacles[i][1]:
                    current_hori_left_obs = obstacles[i]
        if obstacles[i][1] == c_q:  # sam col
            if obstacles[i][0] > r_q:  # check vert up
                if current_vert_up_obs is None or current_vert_up_obs[0] > obstacles[i][0]:
                    current_vert_up_obs = obstacles[i]
            if obstacles[i][0] < r_q:  # check vert down
                if current_vert_down_obs is None or current_vert_down_obs[0] < obstacles[i][0]:
                    current_vert_down_obs = obstacles[i]
        if obstacles[i][0] - r_q == obstacles[i][1] - c_q:  # same front slash
            if obstacles[i][0] > r_q:  # check front up
                if current_front_up_obs is None or current_front_up_obs[0] > obstacles[i][0]:
                    current_front_up_obs = obstacles[i]
            if obstacles[i][0] < r_q:  # check front down
                if current_front_down_obs is None or current_front_down_obs[0] < obstacles[i][0]:
                    current_front_down_obs = obstacles[i]
        if obstacles[i][0] - r_q == c_q - obstacles[i][1]:  # same back slash
            if obstacles[i][0] > r_q:  # check front up
                if current_back_up_obs is None or current_back_up_obs[0] > obstacles[i][0]:
                    current_back_up_obs = obstacles[i]
            if obstacles[i][0] < r_q:  # check front down
                if current_back_down_obs is None or current_back_down_obs[0] < obstacles[i][0]:
                    current_back_down_obs = obstacles[i]

    all_hori = 0
    all_vert = 0
    all_front_slash = 0
    all_back_slash = 0

    if current_hori_right_obs is not None:
        all_hori += (current_hori_right_obs[1] - c_q - 1)
    else:
        all_hori += (n - c_q)
    if current_hori_left_obs is not None:
        all_hori += (c_q - current_hori_left_obs[1] - 1)
    else:
        all_hori += (c_q - 1)
    if current_vert_up_obs is not None:
        all_vert += (current_vert_up_obs[0] - r_q - 1)
    else:
        all_vert += (n - r_q)
    if current_vert_down_obs is not None:
        all_vert += (r_q - current_vert_down_obs[0] - 1)
    else:
        all_vert += (r_q - 1)
    if current_front_up_obs is not None:
        all_front_slash += (current_front_up_obs[0] - r_q - 1)
    else:
        all_front_slash += min(n - r_q, n - c_q)
    if current_front_down_obs is not None:
        all_front_slash += (r_q - current_front_down_obs[0] - 1)
    else:
        all_front_slash += min(r_q - 1, c_q - 1)
    if current_back_up_obs is not None:
        all_back_slash += (current_back_up_obs[0] - r_q - 1)
    else:
        all_back_slash += min(n - r_q, c_q - 1)
    if current_back_down_obs is not None:
        all_back_slash += (r_q - current_back_down_obs[0] - 1)
    else:
        all_back_slash += min(r_q - 1, n - c_q)

    return all_hori + all_vert + all_front_slash + all_back_slash


nk = input().split()
n = int(nk[0])
k = int(nk[1])
r_qC_q = input().split()
r_q = int(r_qC_q[0])
c_q = int(r_qC_q[1])
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)

print(result)
