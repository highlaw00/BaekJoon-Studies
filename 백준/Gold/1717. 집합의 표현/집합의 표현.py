import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

n, m = map(int, input().split())

uf = [i for i in range(n+1)]

# union 함수는 x의 조상 노드가 y의 조상 노드를 가리키도록 하는 함수
# 즉, x의 조상 노드를 찾고, y의 조상 노드를 찾은 뒤
# uf[x 조상] = y 조상 을 실행한다


def union(x, y):
    x_ancestor, y_ancestor = find(x), find(y)
    uf[x_ancestor] = y_ancestor


def find(x):
    if x == uf[x]:  # x가 루트 노드인 경우
        return x    # 루트 노드를 반환
    root_node = find(uf[x])  # 루트 노드가 아니라면 조상 노드를 재귀적으로 찾는다
    uf[x] = root_node        # 이후 조상 노드를 현재 노드의 부모 노드로 만든다
    return root_node


for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
    else:
        union(a, b)
