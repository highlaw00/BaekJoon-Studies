import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_010)

t = int(input().rstrip())


def dfs(parent_v):
    global graph, has_color, visited, order
    next_v = graph[parent_v]
    # 다음 노드에 색깔이 존재하면 여태까지 방문한 모든 노드가 사이클이 될 수 없음
    # DFS 더 이상 진행하지 않음
    if has_color[next_v]:
        for v in order:
            has_color[v] = -1
    # 사이클 존재
    elif next_v in visited:
        # order 배열 순회하며 next_v 이전의 노드의 색상을 -1
        # next_v 이후 노드의 색상을 1
        flag = False
        for v in order:
            if v == next_v:
                has_color[v] = 1
                flag = True
                continue
            if flag:
                has_color[v] = 1
            else:
                has_color[v] = -1
    # 다음 노드에 색깔이 없고 방문하지도 않았다면 DFS 진행
    else:
        visited.add(next_v)
        order.append(next_v)
        dfs(next_v)


for _ in range(t):
    n = int(input().rstrip())
    # graph[i] => i 정점이 가리키는 다음 정점
    graph = [0] + list(map(int, input().rstrip().split()))
    # 색깔 배열
    has_color = [0 for _ in range(n+1)]

    # DFS를 모든 정점을 루트로 진행

    for i in range(1, n+1):
        # 만약 루트 노드가 색깔이 존재하면 해당 노드는 생략
        # 루트 노드의 색깔이 0일 때만 DFS 진행
        if not has_color[i]:
            visited = set()
            visited.add(i)
            order = [i]
            dfs(i)

    ans = has_color.count(-1)
    print(ans)
