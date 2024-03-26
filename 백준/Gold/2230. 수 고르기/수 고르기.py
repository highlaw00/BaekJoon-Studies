import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = sorted([int(input()) for _ in range(n)])

minVal = sys.maxsize

left = 0
right = 1

# 두 포인터가 모두 마지막 숫자를 가리키면 종료
while not (left == n-1 and right == n-1):
    # left와 right가 같은 숫자를 가리킬 때
    if left == right:
        right += 1
        continue
    
    l_num = l[left]
    r_num = l[right]

    diff = abs(l_num - r_num)

    # 정답 후보가 갱신되는 경우
    if diff >= m and minVal > diff:
        minVal = diff
    
    # right가 끝에 도달한 경우 left 증가
    if right == n - 1:
        left += 1
        continue
    
    # 두 숫자의 차이가 m보다 큰 경우: 왼쪽 증가
    if diff > m:
        left += 1
    # 두 숫자의 차이가 m보다 작은 경우: 오른쪽 증가
    elif diff < m:
        right += 1
    # 두 숫자의 차이가 정확히 m이라면: 끝
    else:
        break

print(minVal)