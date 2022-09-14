import sys
while True:
    string = sys.stdin.readline().rstrip()
    if string == '#':
        break
    cnt = 0
    for i in range(len(string)):
        s = string[i]
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
            cnt += 1
    print(cnt)
