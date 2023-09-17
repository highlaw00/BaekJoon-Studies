import heapq
import sys
input = sys.stdin.readline

n = int(input())
state_map = dict()
pq = []
for _ in range(n):
    x = int(input())
    if x:
        state_map[x] = state_map.get(x, 0) + 1
        heapq.heappush(pq, abs(x))
    else:
        if pq:
            minimum = heapq.heappop(pq)
            # -x가 여전히 존재하는 경우
            if -minimum in state_map and state_map[-minimum] > 0:
                state_map[-minimum] -= 1
                print(-minimum)
            # 존재하지 않는 경우
            else:
                print(minimum)
        else:
            print(0)
