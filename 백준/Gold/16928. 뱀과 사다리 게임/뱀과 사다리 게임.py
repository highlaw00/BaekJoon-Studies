import sys
from collections import deque
INT_MAX = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
visited = [0 for _ in range(101)]
ladders = dict()
snakes = dict()

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    ladders[x] = y
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    snakes[u] = v

# 1번부터 BFS 진행
# 갈 수 있는 칸(6칸 이내)을 큐에 삽입한다.
q = deque()
# 큐에 (노드, 현재 굴린 주사위의 수)를 삽입
q.append((1, 0))
visited[1] = 1

ans = 0
while q:
    curr_v, rolled_cnt = q.popleft()
    if curr_v == 100:
        ans = rolled_cnt

    for i in range(1, 7):
        next_v = curr_v + i
        if next_v > 100:
            break
        if not visited[next_v]:
            visited[next_v] = 1
            # 뱀과 연결되었다면 뱀의 끝으로 이동
            if next_v in snakes:
                end_v = snakes[next_v]
                if not visited[end_v]:
                    visited[end_v] = 1
                    q.append((end_v, rolled_cnt + 1))
                continue
            # 사다리와 연결되었다면 사다리의 끝으로 이동
            if next_v in ladders:
                end_v = ladders[next_v]
                if not visited[end_v]:
                    visited[end_v] = 1
                    q.append((end_v, rolled_cnt + 1))
                continue
            q.append((next_v, rolled_cnt + 1))

print(ans)
