# 회의 끝나는 시간을 기준으로 정렬
# 끝나는 시간이 가장 작은 것을 고르고, 그 끝나는 시간 이후 시작하는 시간 중 가장 끝나는 시간이 작은 것을 선택

import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    s, e = map(int, input().rstrip().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
# 초기 조건 삽입
last_end_time = meetings[0][1]

for i in range(1, n):
    curr_start_time, curr_end_time = meetings[i]
    # 시작 시간이 마지막 회의 시간 이후라면
    if curr_start_time >= last_end_time:
        cnt += 1
        last_end_time = curr_end_time

print(cnt)
