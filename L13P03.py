def binary_search(_arr, _x):
    head = 0
    tail = len(_arr)-1
    mid_point = int((head + tail)/2)
    while head < tail:
        if _arr[mid_point] == _x:
            return mid_point
        elif _arr[mid_point] < _x:
            return mid_point + 1 + binary_search(_arr[mid_point+1:], _x)
        else:
            return binary_search(_arr[:mid_point], _x)
    if _arr[mid_point] != _x:
        print(-1)
        exit()
    else:
        return mid_point


n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(binary_search(arr, x) + 1)
