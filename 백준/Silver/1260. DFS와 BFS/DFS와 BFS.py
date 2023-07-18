from collections import deque
# 정점의 개수, 간선의 개수, 시작 간선이 주어졌을 때, dfs, bfs의 탐색 과정을 출력하라
n, m, v = map(int, input().split())

# 우선 그래프부터 입력 받고
# 그래프를 오름차순으로 정렬하고
# dfs 수행 결과와 bfs 수행결과 출력
# 양방향 그래프 => 반대에도 넣어줘야함

g = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

for i in range(n+1):
    g[i].sort()


def dfs(root):
    global g, visited
    for next in g[root]:
        # 방문하지 않은 정점을 방문
        if not visited[next]:
            visited[next] = 1
            print(next, end=' ')
            dfs(next)


# dfs 수행
visited = [0 for _ in range(n+1)]
visited[v] = 1
print(v, end=' ')
dfs(v)


print()


def bfs():
    global q, visited
    while q:
        curr = q.popleft()
        for next in g[curr]:
            if not visited[next]:
                visited[next] = 1
                print(next, end=' ')
                q.append(next)


# bfs 수행
q = deque()
visited = [0 for _ in range(n+1)]
visited[v] = 1
q.append(v)
print(v, end=' ')
bfs()
