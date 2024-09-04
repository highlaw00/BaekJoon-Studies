def avail_and_max(k, dp, times):
    avails = []
    for i in range(1, 11):
        if k-i < 0: 
            continue
        elif k-i + times[k-i] <= k:
            avails.append(k-i)
            
    if len(avails) == 0:
        return 0
    
    max_val = dp[avails[0]]
    for val in avails:
        max_val = max(max_val, dp[val])
        
    return max_val

n = int(input())
times = []
prices = []
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)

# f(k) = k번째 날 상담을 진행할 때, 얻을 수 있는 최대 수익
dp = [0 for _ in range(n)]

for i in range(n):
    # f(k) = avail_and_max(f(k-1), f(k-2), f(k-3), f(k-4), f(k-5)) + Pk
    # 만약 k번째 날 상담을 진행할 수 없는 경우 Pk는 제외함
    if i + times[i] > n:
        dp[i] = avail_and_max(i, dp, times)
    else:
        dp[i] = avail_and_max(i, dp, times) + prices[i]

print(max(dp))