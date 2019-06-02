# Problem from ACM TIMUS
# http://acm.timus.ru/problem.aspx?space=1&num=2002


def solution():
    n = int(input())
    users = {}
    for i in range(n):
        operation_line = list(map(str, input().split()))
        if operation_line[0] == 'register':
            if users.get(operation_line[1]) is not None:
                print('fail: user already exists')
            else:
                users[operation_line[1]] = [operation_line[2], 'out']
                print('success: new user added')

        if operation_line[0] == 'login':
            user_identity = users.get(operation_line[1])
            if user_identity is None:
                print('fail: no such user')
            else:
                if user_identity[0] == operation_line[2]:
                    if user_identity[1] == 'out':
                        users.get(operation_line[1])[1] = 'in'
                        print('success: user logged in')
                    else:
                        print('fail: already logged in')
                else:
                    print('fail: incorrect password')
        if operation_line[0] == 'logout':
            user_identity = users.get(operation_line[1])
            if user_identity is None:
                print('fail: no such user')
            elif user_identity[1] == 'out':
                print('fail: already logged out')
            else:
                user_identity[1] = 'out'
                print('success: user logged out')


solution()
