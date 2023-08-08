n, k = map(int, input().split())
l = []

for _ in range(n):
    w, v = map(int, input().split())
    l.append((w, v))

# dp[i] => 최대로 담을 수 있는 무게가 i일 때, 담을 수 있는 최대 가치
dp = [0 for _ in range(k+1)]
# 우선 리스트를 무게를 기준으로 오름차순 한 뒤, 하나씩 순회하며 dp테이블을 갱신한다
l.sort()

# 그리고, dp[i]값이 0이 아닌 인덱스를 담을 리스트를 하나 선언한다
non_zero = set()
visited = []


for i in range(n):
    new_non_zero = []
    curr_weight, curr_val = l[i]

    if curr_weight > k:
        continue

    for j in visited:
        if j + curr_weight > k:
            continue
        dp[j+curr_weight] = max(dp[j+curr_weight], dp[j] + curr_val)
        new_non_zero.append(j+curr_weight)

    dp[curr_weight] = max(dp[curr_weight], curr_val)

    new_non_zero.append(curr_weight)

    for num in new_non_zero:
        non_zero.add(num)
    visited = list(non_zero)
    # 내림차순으로 하는 이유? 갱신한 것을 재 참조할 가능성이 있기 때문
    visited.sort(key=lambda x: -x)

print(max(dp))
