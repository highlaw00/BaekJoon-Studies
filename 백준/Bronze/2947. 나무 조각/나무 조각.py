l = list(map(int,input().split()))

for i in range(4):
    #print('i: ',i)
    for j in range(4):
        #print('j: ',j)
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            print('%d %d %d %d %d'%(l[0], l[1], l[2], l[3], l[4]))