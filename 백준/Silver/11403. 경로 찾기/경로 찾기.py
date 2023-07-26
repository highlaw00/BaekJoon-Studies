# BFS를 모든 정점에 대해 진행
# BFS하며 방문하는 모든 정점을 기록
# 자기 자신은 처음에 방문했다고 치지 않음.
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = []
q = deque()


def bfs():
    global q
    while q:
        curr = q.popleft()
        for i in range(n):
            # 방문하지 않았으며 연결되어 있다면 큐에 삽입
            if graph[curr][i] and not visited[i]:
                visited[i] = 1
                q.append(i)


# n개의 node에 대해서 BFS를 진행합니다.
for i in range(n):
    visited = [0 for _ in range(n)]
    q.append(i)
    bfs()
    ans.append(visited)

for row in ans:
    print(' '.join(map(str, row)))
