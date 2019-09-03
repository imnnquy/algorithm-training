#  Problem from SPOJ
#  https://www.spoj.com/problems/LAZYPROG/


import heapq


class Project:
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d

    def __lt__(self, other):
        return self.a > other.a


def solution():
    t = int(input())

    for i in range(t):
        sum_money = 0
        initial_time = 0
        priority_queue = []
        projects = []
        n = int(input())
        for j in range(n):
            a, b, d = map(int, input().strip().split())
            projects.append(Project(a, b, d))
        projects.sort(key=lambda x: x.d, reverse=False)

        for j in range(n):
            initial_time += projects[j].b
            heapq.heappush(priority_queue, projects[j])
            if initial_time <= projects[j].d:
                continue
            while True:
                pop_project = heapq.heappop(priority_queue)
                if initial_time - pop_project.b <= projects[j].d:
                    pop_project.b -= initial_time-projects[j].d
                    sum_money += (initial_time-projects[j].d) / pop_project.a
                    initial_time = projects[j].d
                    heapq.heappush(priority_queue, pop_project)
                    break

                else:
                    sum_money += pop_project.b / pop_project.a
                    initial_time -= pop_project.b

        print("{0:.2f}".format(sum_money))


solution()
