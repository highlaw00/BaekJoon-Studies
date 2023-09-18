# 0-1 bfs

# x-1 or x+1 -> 1초 소모
# 2*x -> 0초 소모

# n -> k 까지 이동하는 최단 거리
import sys
from collections import deque
INT_MAX = sys.maxsize

n, k = map(int, input().split())
ans = INT_MAX
if n >= k:
    ans = n - k
else:
    ARR_SIZE = n + k
    dists = [INT_MAX for _ in range(ARR_SIZE + 1)]
    dq = deque()
    dq.append(n)
    dists[n] = 0
    while dq:
        x = dq.popleft()
        dist_so_far = dists[x]

        if x == k:
            ans = dist_so_far
            break

        for next_x in (x+1, x-1, 2*x):
            if next_x > ARR_SIZE or next_x < 0:
                continue
            weight = 0 if next_x == 2*x else 1
            # relax 되면 append
            if dists[next_x] > dist_so_far + weight:
                dists[next_x] = dist_so_far + weight
                if next_x == 2*x:
                    dq.appendleft(next_x)
                else:
                    dq.append(next_x)

print(ans)
