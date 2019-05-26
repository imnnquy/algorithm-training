# Problem from ACM TIMUS
# http://acm.timus.ru/problem.aspx?space=1&num=1837


INF = int(1e9)


def solution():
    players = {'Isenbaev': 0}
    n_teams = int(input())
    for i in range(n_teams):
        players_line = input().split()
        if players.get(players_line[0]) is None:
            players[players_line[0]] = INF
        min_proximity = players[players_line[0]]
        min_index = 0
        for j in range(1, len(players_line)):
            if players.get(players_line[j]) is None:
                players[players_line[j]] = INF
            if min_proximity > players[players_line[j]]:
                min_proximity = players[players_line[j]]
                min_index = j
        if min_proximity < INF:
            for j in range(len(players_line)):
                if j is not min_index and players[players_line[j]] > min_proximity:
                    players[players_line[j]] = min_proximity + 1

    for key in sorted(players.keys()):
        proximity = str(players[key]) if players[key] is not INF else 'undefined'
        print(key + ' ' + proximity)


solution()
