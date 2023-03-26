n = int(input())

arr = [0] + list(map(int, input().split()))

prefix = [0]

for i in range(1, n + 1):
    prefix.append(max(prefix[i - 1] + arr[i], arr[i]))

print(max(prefix[1:]))
