import sys
sys.setrecursionlimit(126000)
input = sys.stdin.readline

n = int(input().rstrip())
costs = [0 for _ in range(n+1)]
requirements = [[] for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().rstrip().split()))
    cost = line[0]
    costs[i] = cost
    # update requirements
    for j in range(1, len(line) - 1):
        requirements[i].append(line[j])

dp = [-1 for _ in range(n+1)]
# from root, get value of dp[v]. v is requirements of root node
# if dp[v] is not available, dfs that v node too.


def get_cost(root):
    requirements_cost = 0
    for v in requirements[root]:
        # if dp[v] is not available, dfs that v node too.
        # also save the return value of dfs at dp[v]
        if dp[v] == -1:
            dp[v] = get_cost(v)
        requirements_cost = max(requirements_cost, dp[v])
    return requirements_cost + costs[root]


# get_cost of every nodes
for i in range(1, n+1):
    if dp[i] == -1:
        dp[i] = get_cost(i)
    print(dp[i])
