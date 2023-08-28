import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
tree = [[] for _ in range(n)]
root = 0

for i, parent_node in enumerate(l):
    if parent_node != -1:
        # parent_node -> i 가리키기
        tree[parent_node].append(i)
    else:
        root = i

target = int(input().rstrip())

# 모든 노드를 탐색하며 target을 가리키는 간선 삭제
if root != target:
    for children in tree:
        if target in children:
            index = children.index(target)
            del children[index]
            break

# root 부터 bfs 진행하며 자식이 없는 경우 정답 개수를 증가시킴
ans = 0
q = deque()
if root != target:
    q.append(root)
while q:
    parent = q.popleft()
    # 자식이 존재할 경우
    if tree[parent]:
        for child in tree[parent]:
            q.append(child)
    # 리프 노드인 경우
    else:
        ans += 1

print(ans)
