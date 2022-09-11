t = int(input())

for i in range(t):
    c, v = map(int, input().split())
    q = int(c / v)
    r = c % v
    print("You get {} piece(s) and your dad gets {} piece(s).".format(q,r))