# 플로이드 워셜
# 어떤 노드 s와 e가 존재할 때, s부터 e까지 가는 최단거리는 다음과 같다.
# d[s][e] = min(d[s][e], d[s][m] + d[m][e])
# m은 s와 e 사이에 존재하는 모든 노드이다.
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().rstrip().split())
dist = [[INF for _ in range(n)] for _ in range(n)]

# 자기 자신까지의 거리는 항상 0임
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    # a, b는 직접 연결되어있음
    a, b = map(int, input().rstrip().split())
    a, b = a - 1, b - 1
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드 워셜 알고리즘을 실행
for curr_node in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i]
                             [curr_node] + dist[curr_node][j])

ans = 0
val = INF

for i, row in enumerate(dist):
    kevin_dist = sum(row)
    if kevin_dist < val:
        ans = i
        val = kevin_dist

print(ans + 1)
