# Problem from CodeChef
# https://www.codechef.com/problems/RRATING


import heapq


def solution():
    top_reviews = []
    candidate_reviews = []
    N = int(input())
    results = []
    num_of_reviews = 0
    for i in range(N):
        command = input().strip()
        if command.startswith('1'):
            num_of_reviews += 1
            new_review = int(command.split()[1])
            if len(top_reviews) < num_of_reviews // 3:
                if len(candidate_reviews) < 0 or new_review > -candidate_reviews[0]:
                    heapq.heappush(top_reviews, new_review)
                else:
                    heapq.heappush(top_reviews, -candidate_reviews[0])
                    heapq.heappop(candidate_reviews)
                    heapq.heappush(candidate_reviews, -new_review)
            else:
                if len(top_reviews) > 0 and new_review > top_reviews[0]:
                    heapq.heappush(candidate_reviews, -top_reviews[0])
                    heapq.heappop(top_reviews)
                    heapq.heappush(top_reviews, new_review)
                else:
                    heapq.heappush(candidate_reviews, -new_review)
        else:
            if len(top_reviews) > 0:
                results.append(top_reviews[0])
            else:
                results.append('No reviews yet')

    print(*results, sep='\n')


solution()
