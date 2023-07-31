import sys
input = sys.stdin.readline
n = int(input())
ans = 0

for _ in range(n):
    scores = list(map(int, input().rstrip().split()))
    runs = scores[0:2]
    tricks = scores[2:]
    n1 = max(runs)
    tricks.sort(key=lambda x: -x)
    n2, n3 = tricks[0], tricks[1]
    ans = max(ans, n1+n2+n3)
print(ans)
