n = int(input())
memo = [1, 1, 3]

for i in range(3, n+1):
    curr = memo[i-1] + memo[i-2] * 2
    memo.append(curr)

print(memo[n] % 10007)
