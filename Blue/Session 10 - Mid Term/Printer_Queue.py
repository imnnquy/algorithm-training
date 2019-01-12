
def solution():
    tcs = int(input())
    for i in range(tcs):
        n, m = map(int, input().split())
        printer_queue = list(map(int, input().split()))
        sorted_list = sorted(printer_queue, reverse=True)
        counter = 0
        pointer = 0
        largest_pos = 0
        while True:
            if largest_pos >= n:
                break

            if printer_queue[pointer] == sorted_list[largest_pos]:
                counter += 1
                largest_pos += 1
                if pointer == m:
                    break
            else:
                if pointer == m:
                    m = len(printer_queue)
                printer_queue.append(printer_queue[pointer])

            pointer += 1

        print(counter)


solution()
