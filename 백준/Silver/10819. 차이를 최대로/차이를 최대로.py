from itertools import permutations as pm

n = int(input())
arr = list(map(int, input().split()))

ans = min(arr)

for elem in pm(arr, n):
    temp_sum = 0

    for i in range(len(elem)-1):
        prev = i
        curr = i + 1
        temp_sum += abs(elem[prev] - elem[curr])

    if temp_sum > ans:
        ans = temp_sum

print(ans)
