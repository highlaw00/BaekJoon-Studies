import sys
INT_MAX = sys.maxsize

n = int(input())
m = int(input())
if m:
    s = set(map(int, input().split()))
else:
    s = set()

# 0부터 N까지 거리 테이블 생성
dp = [INT_MAX for _ in range(2*500_000+1)]

# 고장난 버튼을 사용해서 만들 수 있는 모든 경우의 거리를 갱신
# 단, 100은 제외
for i in range(2*500_000+1):
    temp = i
    if temp == 0:
        if 0 not in s:
            dp[0] = 1
        continue
    flag = True
    cnt = 0
    while temp != 0:
        ones = temp % 10
        temp = temp // 10
        if ones in s:
            flag = False
            break
        else:
            cnt += 1
    if flag:
        dp[i] = cnt
dp[100] = 0
# 정답은 최소한 100번에서 N까지 +,-를 눌러 가는 경우
ans = min(dp[n], abs(n - 100))
# N부터 -1씩하며 가장 가까운 버튼을 눌러 갈 수 있는 곳을 탐색 (TO 0)
for i in range(n - 1, -1, -1):
    if dp[i] != INT_MAX:
        ans = min(ans, dp[i] + abs(n-i))
        break

# N부터 +1씩하며 가장 가까운 버튼을 눌러 갈 수 있는 곳을 탐색 (TO 2*N)
for i in range(n + 1, len(dp)):
    if dp[i] != INT_MAX:
        ans = min(ans, dp[i] + abs(n-i))
        break

print(ans)
