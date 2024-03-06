# DFS: 깊이 우선 탐색

# 1. 그래프를 입력한다.
# 2. 정점을 방문한다.
# 3. 연결된 정점 중 방문하지 않은 정점을 탐색한다.
# 3-1. 만약 없다면 반환한다
# 3-2. 만약 있다면 해당 정점으로 재귀한다.
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

# graph[i] = 정점 i와 연결된 정점들
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    s, d = map(int, input().split())
    graphs[s].append(d)
    graphs[d].append(s)

# 오름차순으로 방문하기 위해 그래프 정렬
for i in range(len(graphs)):
    graphs[i].sort()

visited = [False for _ in range(n+1)]

def dfs(root):
    global visited, graphs
    # 방문 처리
    visited[root] = True
    print(root, end=" ")
    # 연결 간선 확인
    for vertex in graphs[root]:
        # 방문하지 않은 정점이 있다면 재귀
        if not visited[vertex]:
            dfs(vertex)

dfs(v)
print()

# bfs: 너비 우선 탐색

# 1. 현재 정점을 방문한다.
# 2. 연결된 정점 중 방문하지 않은 정점을 모두 큐에 삽입한다.
# 3. 큐에 있는 정점을 pop 하며 탐색을 진행

q = deque()
visited = [False for _ in range(n+1)]

q.append(v)
while q:
    root = q.popleft()
    # 방문한 적이 있다면 스킵
    if visited[root]:
        continue
    visited[root] = True
    print(root, end=" ")
    for vertex in graphs[root]:
        if not visited[vertex]:
            q.append(vertex)

