import sys

n, h = map(int, input().split())
# n은 항상 짝수
arr = [0 for _ in range(h+1)]  # 양 끝에 패딩
for i in range(1, n+1):
    tmp = int(sys.stdin.readline().rstrip())
    if i % 2 != 0:
        # 석순
        arr[1] += 1
        arr[tmp + 1] -= 1
    else:
        # 종유석
        arr[h-tmp + 1] += 1

for i in range(1, h+1):
    arr[i] += arr[i-1]

arr = arr[1:]
ans = min(arr)
ans_cnt = 0
for i in range(0, h):
    if arr[i] == ans:
        ans_cnt += 1

print(ans, ans_cnt)
