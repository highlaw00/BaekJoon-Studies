N, M, k = map(int, input().split())
ans = 0
for i in range(k + 1):
    n = N - i  # 여학생 중 N-i명이 인턴에 참가
    m = M - (k - i)  # 남학생이 나머지 인턴 자리를 메꿈
    t = min(n // 2, m)  # 만들어지는 팀의 개수
    if t >= ans:
        ans = t
print(ans)
