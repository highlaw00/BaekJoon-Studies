idx = 0
while (True):
    idx += 1
    flag = False
    o, w = map(int,input().split())
    if o == 0 and w == 0: break
    
    while (True):
        act, num = map(str,input().split())
        if act == '#' and num == '0': break # 상태 출력
        num = int(num)
        if act == 'E': w -= num
        else: w += num
        if w <= 0: flag = True
        
    if flag: print('{} RIP'.format(idx))
    elif o / 2 < w < 2 * o: print('{} :-)'.format(idx))
    else: print('{} :-('.format(idx))