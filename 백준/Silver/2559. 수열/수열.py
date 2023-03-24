import sys

n, k = map(int, input().split())

arr = [0] + list(map(int, sys.stdin.readline().split()))

prefix = [0]
maxi = -sys.maxsize

for i in range(1, n - k + 2):
    if i == 1:
        curr = 0
        for j in range(1, k + 1):
            curr += arr[j]
        prefix.append(curr)
        maxi = curr
    else:
        curr = prefix[i - 1] - arr[i - 1] + arr[i + k - 1]
        prefix.append(curr)
        maxi = max(maxi, curr)


print(maxi)
