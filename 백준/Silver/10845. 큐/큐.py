from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    command = input().rstrip()

    if command.startswith("push"):
        _, x = command.split()
        x = int(x)
        q.append(x)
    elif command.startswith('pop'):
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command.startswith('size'):
        print(len(q))
    elif command.startswith('empty'):
        if q:
            print(0)
        else:
            print(1)
    elif command.startswith('front'):
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
