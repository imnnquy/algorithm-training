# BLUE_LEC18P01


def solution():
    N = int(input())

    tasks = list(map(int, input().split()))

    markers = {}

    for i in range(N):
        if markers.get(tasks[i]) is None:
            markers[tasks[i]] = []
        markers[tasks[i]].append(i)

    possible = False
    possible_count = 1
    for marker in markers.values():
        if len(marker) == 2:
            possible_count *= 2
            if possible_count >= 3:
                possible = True
                break

        elif len(marker) >= 3:
            possible = True
            break

    if not possible:
        print('NO')
        return

    tasks.sort()

    for i in range(3):
        flag = {}
        for j in range(N):
            if flag.get(j) is None:
                flag[j] = 0
            print(markers[tasks[j]][flag[j] % len(markers[tasks[j]])] + 1, end='')
            flag[j] += 1
        print()


solution()
