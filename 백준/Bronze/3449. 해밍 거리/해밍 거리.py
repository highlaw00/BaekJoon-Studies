t = int(input())

for _ in range(t):
    n1 = input()
    n2 = input()
    cnt = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            cnt += 1
    print('Hamming distance is {}.'.format(cnt))