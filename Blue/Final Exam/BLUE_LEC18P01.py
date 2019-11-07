# BLUE_LEC18P01


def solution():
    N = int(input())

    tasks = list(map(int, input().split()))

    markers = {}

    for i in range(N):
        if markers.get(tasks[i]) is None:
            markers[tasks[i]] = [1]
        markers[tasks[i]].append(i)

    possible = False
    possible_count = 1

    duplications = []
    duplicated_keys = []
    for key, marker in markers.items():
        if len(marker) == 3:
            possible_count *= 2
            duplications.append(marker)
            duplicated_keys.append(key)
            if possible_count >= 3:
                possible = True
                break

        elif len(marker) >= 4:
            possible = True
            duplications = [marker]
            duplicated_keys = [key]
            break

    if not possible:
        print('NO')
        return

    print('YES')
    tasks.sort()

    if len(duplications) == 2:

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][1] = markers[duplicated_keys[0]][1], \
                                                                         markers[duplicated_keys[0]][2]

        for marker in markers.values():
            marker[0] = 1
        print()
        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1
        for marker in markers.values():
            marker[0] = 1
        print()

        markers[duplicated_keys[1]][2], markers[duplicated_keys[1]][1] = markers[duplicated_keys[1]][1], \
                                                                         markers[duplicated_keys[1]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

    if len(duplications) == 1:
        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

        print()
        for marker in markers.values():
            marker[0] = 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][1] = markers[duplicated_keys[0]][1], \
                                                                         markers[duplicated_keys[0]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1

        print()
        for marker in markers.values():
            marker[0] = 1
        markers[duplicated_keys[0]][2], markers[duplicated_keys[0]][3] = markers[duplicated_keys[0]][3], \
                                                                         markers[duplicated_keys[0]][2]

        for i in range(N):
            print(markers[tasks[i]][markers[tasks[i]][0]] + 1, end=' ')
            if markers[tasks[i]][0] == len(markers[tasks[i]]) - 1:
                markers[tasks[i]][0] = 1
            else:
                markers[tasks[i]][0] += 1


solution()
