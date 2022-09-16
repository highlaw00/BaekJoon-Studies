l = list(map(int, input().split()))
last_num = l[0]
flag = True

for i in range(1, len(l)):
    curr_num = l[i]
    if last_num > curr_num:
        flag = False
    last_num = curr_num

if flag:
    print('Good')
else:
    print('Bad')
