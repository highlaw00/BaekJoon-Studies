from collections import deque
import sys

def solution(x, y, n):
    # 1. 현재 위치에서 n 더하기
    # 2. 현재 위치에서 2 곱하기
    # 3. 현재 위치에서 3 곱하기
    answer = sys.maxsize
    visited = [False for _ in range(0, y + 1)]
    dist = [sys.maxsize for _ in range(0, y + 1)]
    queue = deque()
    queue.append(x)
    
    dist[x] = 0
    
    while queue:
        curr = queue.popleft()
        if visited[curr]: continue
        visited[curr] = True
        # dist[curr + something] = min(dist[curr + something], dist[curr] + 1)
        # n 더하는 경우
        if curr + n <= y:
            dist[curr + n] = min(dist[curr + n], dist[curr] + 1)
            queue.append(curr + n)
        if curr * 2 <= y:
            dist[curr * 2] = min(dist[curr * 2], dist[curr] + 1)
            queue.append(curr * 2)
        if curr * 3 <= y:
            dist[curr * 3] = min(dist[curr * 3], dist[curr] + 1)
            queue.append(curr * 3)
    
    answer = dist[y]
    if answer == sys.maxsize:
        answer = -1
    
    return answer