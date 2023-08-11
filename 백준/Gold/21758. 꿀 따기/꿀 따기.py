import sys
input = sys.stdin.readline
n = int(input().rstrip())

A = [0] + list(map(int, input().rstrip().split()))
L = [0 for _ in range(n+1)]
R = [0 for _ in range(n+1)]

# 왼쪽 누적합 선언
for i in range(1, n+1):
    L[i] = L[i-1] + A[i]

# 오른쪽 누적합 선언
R[-1] = A[-1]
for i in range(n-1, 0, -1):
    R[i] = R[i+1] + A[i]

ans = 0

# t의 위치를 처음부터 끝까지 조정하며 최대값을 탐색합니다.
# 단, t가 양 끝에 존재할 땐 꿀벌1은 그 반대편에 존재하며, 꿀벌2의 후보지를 O(n) 시간 내 탐색합니다.
# t가 만약 양 끝에 존재하지 않으면 양 끝에 꿀벌1,2 를 배치하고 답을 갱신합니다
for t in range(1, n+1):
    if 1 < t < n:
        # t가 가운데에 존재한다면 양 끝에서부터의 누적합을 구합니다
        candidate = (L[t] - A[1]) + (R[t] - A[-1])
        ans = max(ans, candidate)
    elif t == 1:
        # t가 맨 왼쪽에 있다면 꿀벌1은 맨 오른쪽에 위치하고, 꿀벌2의 후보지를 탐색합니다
        # 맨 왼쪽부터 맨 오른쪽까지의 합 - 맨 오른쪽 원소
        sum1 = L[-1] - A[-1]
        for i in range(2, n):
            # 맨 왼쪽부터 맨 오른쪽까지의 합 - 맨 오른쪽 원소 + i-1이전의 합 - i 원소의 값
            candidate = sum1 + L[i-1] - A[i]
            ans = max(ans, candidate)
    else:
        # t가 맨 오른쪽에 있다면 꿀벌1은 맨 왼쪽에 위치하고, 꿀벌2의 후보지를 탐색합니다
        # 맨 왼쪽부터 맨 오른쪽까지의 합 - 맨 왼쪽 원소
        sum1 = L[-1] - A[1]
        for i in range(2, n):
            candidate = sum1 + R[i+1] - A[i]
            ans = max(ans, candidate)

print(ans)
