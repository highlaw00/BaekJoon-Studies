n = int(input())

for i in range(n):
    # i번 공백 출력, n-i번 별표 출력
    for j in range(i):
        print(end=' ')
    for k in range(n-i):
        print(end='*')
    print()
