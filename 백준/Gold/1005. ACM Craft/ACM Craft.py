import sys
sys.setrecursionlimit(1001)
input = sys.stdin.readline


# root와 연결된 모든 노드에 대해서 DFS 진행


def get_cost(root):
    child = []
    for v in graph[root]:
        if dp[v] == -1:
            dp[v] = get_cost(v)
            child.append(dp[v])
        else:
            child.append(dp[v])
    if child:
        return max(child) + costs[root]
    else:
        return costs[root]


t = int(input().rstrip())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    costs = [0] + list(map(int, input().rstrip().split()))
    # 건설순서 x, y
    # 그래프를 역순으로 설정
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[y].append(x)
    w = int(input().rstrip())
    # dp 테이블 초기화
    # dp[i] = i번째 건물을 짓는데 걸리는 최소 시간
    # dp[i] = max(dp[a1] + dp[a2] + ... dp[aj]) + cost[i] || a1,...,aj는 i를 짓기 위해 반드시 지어야하는 건물
    dp = [0] + [-1 for _ in range(n)]

    ans = get_cost(w)
    print(ans)
