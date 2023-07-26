from collections import deque

n, k = map(int, input().split())
visited = [False for _ in range(100_001)]
q = deque()

# 수빈이의 위치에서 bfs 시작
cnt = 0
visited[n] = 1
q.append(n)


def bfs():
    global cnt
    while q:
        for _ in range(len(q)):
            # 현재 위치 pop
            x = q.popleft()
            if x == k:
                return
            # x+1, x-1, 2*x 탐색
            x1, x2, x3 = x - 1, x + 1, x * 2
            if x1 >= 0 and not visited[x1]:
                visited[x1] = 1
                q.append(x1)
            if x2 <= 100_000 and not visited[x2]:
                visited[x2] = 1
                q.append(x2)
            if 0 < x3 <= 100_000 and not visited[x3]:
                visited[x3] = 1
                q.append(x3)
        cnt += 1


bfs()
print(cnt)
