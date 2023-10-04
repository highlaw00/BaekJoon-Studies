import sys
n = int(input())

# 가장 작은 생성자를 찾습니다.
ans = sys.maxsize

for i in range(n, 0, -1):
    # i가 생성자인지 확인합니다.
    summation = i
    # i의 모든 자릿수를 더해보고 그 합이 n과 같은지 확인합니다.
    temp_i = i
    while temp_i != 0:
        summation += temp_i % 10
        temp_i = temp_i // 10
    if summation == n:
        ans = min(ans, i)

if ans == sys.maxsize:
    print(0)
else:
    print(ans)
