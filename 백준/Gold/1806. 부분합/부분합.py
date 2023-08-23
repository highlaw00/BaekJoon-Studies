# 길이 N 짜리 수열
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 s 이상이 되는 것 중,
# 가장 짧은 것의 길이를 구하라
# 각 수는 10000 이하의 자연수로 이루어져있다.

# 투 포인터 기법을 사용해 O(N) 내에 풀 수 있다.

import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

n, s = map(int, input().rstrip().split())
l = list(map(int, input().rstrip().split()))
ans = INT_MAX

j = 0
# cnt: 부분합의 총합을 담는 변수
cnt = l[0]
for i in range(n):
    # 부분합의 총합이 s 이상이 될 때까지
    # 그리고
    # j가 인덱스를 넘어가기 전까지 j를 밀어줍니다
    # j는 0부터 n-1까지
    while cnt < s and j < n-1:
        j += 1
        cnt += l[j]

    # while을 빠져나왔을 땐 다음을 만족합니다
    # 1. 부분합이 s 이상
    # 2. j가 끝까지 가서 더이상 진행할 수 없는 경우
    # 따라서, 부분합의 크기를 보고 결정해주면 됩니다
    if cnt >= s:
        ans = min(ans, j-i+1)

    # i를 당겨줄 땐 cnt에서 i의 값을 빼줘야합니다
    cnt -= l[i]

if ans == INT_MAX:
    print(0)
else:
    print(ans)
