n, m = map(int, input().split())
ans = min((n-1) + (m-1) * n, (m-1) + (n-1) * m)
print(ans)