# a1, a2, ... , an
# 자연수 x에 대해 ai + aj = x (1<=i<j<=n) 을 만족하는 (ai, aj)의 쌍을 구하라

# 1. 전부 정렬하기 nlogn
# 2. s, e 포인터 설정
# 3. s + e 를 해보고, 만약 s + e가 x라면 cnt += 1
# 3-1. 이게 가능한 이유는 ai가 모두 다르기 때문이다.
# 3-2. s 와 e는 모두 한칸씩 당겨 준다.
# 4. s + e 가 x보다 작다면 s를 땡김
# 5. s + e가 x보다 크다면 e를 땡긴다

# 1 2 3 4 5
# s       e

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())
cnt = 0
s, e = 0, n-1

while s < e:
    curr = arr[s] + arr[e]
    if curr == x:
        cnt += 1
        s, e = s + 1, e-1
    elif curr < x:
        s += 1
    else:
        e -= 1

print(cnt)
