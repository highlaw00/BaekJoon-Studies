import math
idx = 0
while(True):
    idx += 1
    l = list(map(int,input().split()))
    if l[0] == 0: break
    r, w, h = l[0], l[1], l[2]
    
    dia = math.sqrt(math.pow(w,2) + math.pow(h,2))
    if dia <= 2 * r:
        print('Pizza {} fits on the table.'.format(idx))
    else:
        print('Pizza {} does not fit on the table.'.format(idx))