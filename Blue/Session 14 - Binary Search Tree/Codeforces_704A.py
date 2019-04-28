# Problem from Codeforces
# http://codeforces.com/problemset/problem/704/A


def solution():
    n, q = map(int, input().strip().split())
    apps = [0 for i in range(n + 1)]
    read_apps = [0 for i in range(n + 1)]
    tmp_read_apps = [0 for i in range(n + 1)]
    noti_list = []
    current_noti = 0
    for i in range(q):
        q1, q2 = map(int, input().split())
        if q1 == 1:
            apps[q2] += 1
            current_noti += 1
            noti_list.append(q2)
        if q1 == 2:
            current_noti -= apps[q2]
            read_apps[q2] += apps[q2]
            apps[q2] = 0
        if q1 == 3:
            max_range = min(q2, len(noti_list))
            for t in range(max_range):
                tmp_read_apps[noti_list[t]] = read_apps[noti_list[t]]
            for t in range(max_range):
                if tmp_read_apps[noti_list[t]] == 0:
                    if apps[noti_list[t]] > 0:
                        current_noti -= 1
                        apps[noti_list[t]] -= 1
                        read_apps[noti_list[t]] += 1
                else:
                    tmp_read_apps[noti_list[t]] -= 1
            for t in range(max_range):
                tmp_read_apps[noti_list[t]] = 0
        print(current_noti)


solution()
