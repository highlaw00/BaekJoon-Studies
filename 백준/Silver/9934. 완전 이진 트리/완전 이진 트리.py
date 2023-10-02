import sys
input = sys.stdin.readline
# full binary tree

k = int(input())
# 노드 개수: 2^k - 1
n = (1 << k) - 1
# 1-index
nodes = [0] + list(map(int, input().rstrip().split()))
tree = [0 for _ in range(n + 1)]
cnt = 1


def in_order(x):
    global cnt
    if x > n:
        return
    # 중위 순회를 합니다.
    in_order(x * 2)
    tree[x] = nodes[cnt]
    cnt += 1
    in_order(x * 2 + 1)


in_order(1)

for i in range(k):
    for j in range(1 << i, 1 << i + 1):
        print(tree[j], end=' ')
    print()
