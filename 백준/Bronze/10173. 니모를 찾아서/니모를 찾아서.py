while True:
    string = input()
    cnt = 0
    if string == 'EOI':
        break
    string = string.upper()
    for i in range(len(string)):
        if string[i] == 'N':
            if i + 4 > len(string):
                continue
            else:
                if string[i:i+4] == 'NEMO':
                    cnt = 1
                    break
    if cnt == 1:
        print('Found')
    else:
        print('Missing')
