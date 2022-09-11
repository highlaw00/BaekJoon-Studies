input = __import__('sys').stdin.readline
n = int(input())
cutecnt = 0
ncutecnt = 0

for i in range(n):
    tmp = int(input())
    if tmp == 0:
        ncutecnt += 1
    else:
        cutecnt += 1

if cutecnt > ncutecnt:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")