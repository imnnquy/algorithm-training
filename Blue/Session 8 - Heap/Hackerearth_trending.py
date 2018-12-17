#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/description/


import heapq


class Topic:

    def __init__(self, topic_id, current_score, posts, likes, comments, shares):
        self.id = topic_id
        self.new_score = posts * 50 + likes * 5 + comments * 10 + shares * 20
        self.change_in_score = self.new_score - current_score

    def __lt__(self, other):
        if self.change_in_score < other.change_in_score:
            return True
        if self.change_in_score == other.change_in_score:
            if self.id < other.id:
                return True
            else:
                return False
        return False


def solution():
    N = int(input())

    top_trends = []
    for i in range(N):
        topic_id, Z, P, L, C, S = map(int, input().strip().split())
        topic = Topic(topic_id, Z, P, L, C, S)

        if i >= 5:
            if top_trends[0] < topic:
                heapq.heappop(top_trends)
                heapq.heappush(top_trends, topic)
        else:
            heapq.heappush(top_trends, topic)

    results = []
    while len(top_trends) > 0:
        topic = heapq.heappop(top_trends)
        results = [str(topic.id) + ' ' + str(topic.new_score)] + results

    print(*results, sep='\n')


solution()
