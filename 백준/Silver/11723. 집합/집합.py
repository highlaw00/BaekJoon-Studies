import sys
input = sys.stdin.readline

m = int(input().rstrip())
s = set()

for _ in range(m):
    cmd = input().rstrip()
    if cmd.startswith('all'):
        s = {i for i in range(1, 21)}
    elif cmd.startswith('empty'):
        s = set()
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd.startswith('add'):
            s.add(x)
        elif cmd.startswith('check'):
            if x in s:
                print(1)
            else:
                print(0)
        elif cmd.startswith('remove'):
            if x in s:
                s.remove(x)
        else:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
