import math as m

n = int(input())
file_list = list(map(int, input().split()))
size = int(input())

clcnt = 0

for i in range(n):
    curr_file = file_list[i]
    if curr_file == 0:
        continue
    clcnt += m.ceil(curr_file/size)

print(clcnt * size)
