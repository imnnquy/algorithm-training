
def solution():
    num_of_chars = int(input())
    checking_string = input().strip()

    checking_array = [False for i in range(26)]

    for i in range(num_of_chars):
        char_index = ord(checking_string[i]) - 65
        if char_index >= 26:
            char_index = ord(checking_string[i]) - 97

        checking_array[char_index] = True

    for i in range(26):
        if not checking_array[i]:
            print('NO')
            return
    print('YES')


solution()
