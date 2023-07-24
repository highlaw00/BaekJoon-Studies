from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
q = deque()
ans = []

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)


def bfs():
    global visited, dist, q, ans, k
    cnt = 0
    sub_q = deque()
    while True:
        cnt += 1
        while q:
            curr = q.popleft()
            for next in graph[curr]:
                if not visited[next]:
                    visited[next] = 1
                    dist[next] = cnt
                    sub_q.append(next)
                    if cnt == k:
                        ans.append(next)
        if not sub_q:
            break
        while sub_q:
            q.append(sub_q.popleft())


# BFS 진행
visited[x] = 1
q.append(x)
bfs()
if ans:
    ans.sort()
    for elem in ans:
        print(elem)
else:
    print(-1)
