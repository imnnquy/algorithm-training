# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1876

#
# Given is an ordered deck of n cards numbered 1
# to n with card 1 at the top and card n at the
# bottom. The following operation is performed as
# long as there are at least two cards in the deck:
# Throw away the top card and move
# the card that is now on the top of the
# deck to the bottom of the deck.
# Your task is to find the sequence of discarded
# cards and the last, remaining card.
# Input
# Each line of input (except the last) contains a
# number n ≤ 50. The last line contains ‘0’ and
# this line should not be processed.
# Output
# For each number from the input produce two
# lines of output. The first line presents the sequence
# of discarded cards, the second line reports
# the last remaining card. No line will have
# leading or trailing spaces. See the sample for the
# expected format.
# Sample Input
# 7
# 19
# 10
# 6
# 0
# Sample Output
# Discarded cards: 1, 3, 5, 7, 4, 2
# Remaining card: 6
# Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14
# Remaining card: 6
# Discarded cards: 1, 3, 5, 7, 9, 2, 6, 10, 8
# Remaining card: 4
# Discarded cards: 1, 3, 5, 2, 6
# Remaining card: 4

import queue

results = []
while True:
    cur_input = int(input())
    if cur_input == 0:
        break

    cur_queue = queue.Queue()
    for i in range(cur_input):
        cur_queue.put(i + 1)
    cur_result = []
    while True:
        if cur_queue.qsize() >= 2:
            cur_result.append(cur_queue.get())
            cur_queue.put(cur_queue.get())
        elif cur_queue.qsize() >= 1:
            cur_result.append(cur_queue.get())
        else:
            break
    results.append(cur_result)

for i in range(len(results)):
    remaining_card = results[i].pop()
    if len(results[i]) > 0:
        end_by = ' '
    else:
        end_by = ''
    print('Discarded cards:', end=end_by)
    print(*results[i], sep=', ')
    print('Remaining card: ' + str(remaining_card))
