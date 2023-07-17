n = int(input())
graph = [list(input()) for _ in range(n)]
friend_1 = [[] for _ in range(n)]
friend_2 = [[] for _ in range(n)]
ans = 0

# 1-친구를 모두 구합니다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Y':
            friend_1[i].append(j)

for i in range(n):
    summary = 0
    for j in friend_1[i]:
        if j not in friend_2[i]:
            summary += 1
            friend_2[i].append(j)
        for k in friend_1[j]:
            if k != i and k not in friend_2[i]:
                summary += 1
                friend_2[i].append(k)
    ans = max(ans, summary)
print(ans)
