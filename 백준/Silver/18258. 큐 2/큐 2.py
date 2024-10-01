from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    # push
    if len(cmd) > 1:
        _, x = cmd
        q.append(int(x))
        continue
    cmd = cmd[0]
    if cmd.startswith("pop"):
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif cmd.startswith("front"):
        if q:
            print(q[0])
        else:
            print("-1")
    elif cmd.startswith("back"):
        if q:
            print(q[-1])
        else:
            print("-1")
    elif cmd.startswith("empty"):
        if q:
            print(0)
        else:
            print(1)
    else:
        print(len(q))