nums = list(map(int, input().split()))
ans = 0
for num in nums:
    ans += int(num ** 2)
ans = ans % 10
print(ans)
