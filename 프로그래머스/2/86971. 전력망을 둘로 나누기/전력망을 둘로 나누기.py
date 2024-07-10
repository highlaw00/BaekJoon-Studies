from collections import deque

def bfs(graphs, visited, start_v):
    queue = deque()
    visited[start_v] = True
    queue.append(start_v)
    vertex_cnt = 0
    while queue:
        curr_v = queue.popleft()
        vertex_cnt += 1
        for next_v in graphs[curr_v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True
    return vertex_cnt

def solution(n, wires):
    answer = 100
    graphs = [[] for _ in range(n+1)]
    # 간선 기록
    for v1, v2 in wires:
        graphs[v1].append(v2)
        graphs[v2].append(v1)
    
    for v1, v2 in wires:
        # 간선 n-1개 중 하나 선택 후 간선 지우기
        graphs[v1].remove(v2)
        graphs[v2].remove(v1)
        
        # 간선 지운 후 bfs를 통해 네트워크 내 노드 개수 탐색
        vertices = []
        visited = [False for _ in range(n+1)]
        for i in range(1, n+1):
            if not visited[i]:
                vertex_amount = bfs(graphs, visited, i)
                vertices.append(vertex_amount)
        gap = abs(vertices[0] - vertices[1])
        answer = min(answer, gap)
        
        # 간선 복구
        graphs[v1].append(v2)
        graphs[v2].append(v1)
    
    return answer