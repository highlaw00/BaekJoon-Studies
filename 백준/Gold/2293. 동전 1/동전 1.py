import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

# k개의 dp 테이블 생성 총 길이 10001 이하
dp = [0 for _ in range(k+1)]

# 숫자(m)을 받으며 다음과 같이 dp 테이블을 갱신
# i를 m의 배수씩 올리면서.. m이 만약 k보다 크다면 무시
# i == m 이라면 dp[i] = dp[i] + 1
# i가 m보다 큰 수라면(배수라면) dp[i] = dp[i] + dp[i-m]
l = []
for _ in range(n):
    x = int(input().rstrip())
    if x > k:
        continue
    l.append(x)

# l 을 내림차순 정렬
l.sort(key=lambda x: -x)

for i in l:
    # i의 배수만큼 k까지 증가시킵니다
    for j in range(i, k+1):
        if j == i:
            dp[j] += 1
            continue
        # 이전 배수의 dp값 만큼 증가
        dp[j] += dp[j-i]

print(dp[k])
