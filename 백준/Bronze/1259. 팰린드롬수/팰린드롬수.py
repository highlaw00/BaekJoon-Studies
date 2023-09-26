while True:
    s = input()
    if s == '0':
        break
    flag = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    if flag:
        print('yes')
    else:
        print('no')
