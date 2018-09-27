inp_str = input()
my_dict = {}
for ch in inp_str:
    if my_dict.get(ch) is None:
        my_dict[ch] = 1
    else:
        print(ch)
        exit()
print('null')
