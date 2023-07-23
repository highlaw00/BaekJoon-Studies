import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input().rstrip())
    arr = input().rstrip().split(',')
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    arr = deque(arr)
    r_flag = False
    e = False
    for c in p:
        if c == 'R':
            r_flag = not r_flag
        elif c == 'D':
            if n == 0:
                e = True
                break
            try:
                if r_flag:
                    arr.pop()
                else:
                    arr.popleft()
            except:
                e = True
                break
    if e:
        print('error')
    else:
        if r_flag:
            arr.reverse()
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr)+']')
