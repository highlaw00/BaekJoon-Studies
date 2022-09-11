t = int(input())

while t:
    n = int(input())
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        p1, p2 = map(str, input().split(' '))
        if p1 == p2:
            continue
        elif (p1 == 'P' and p2 == 'R') or (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P'):
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 > cnt2:
        print('Player 1')
    elif cnt1 < cnt2:
        print('Player 2')
    else:
        print('TIE')
    t -= 1