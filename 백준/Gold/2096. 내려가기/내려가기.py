import sys

input = sys.stdin.readline
n = int(input().rstrip())

mins = [0, 0, 0]
maxs = [0, 0, 0]

for i in range(n):
    scores = list(map(int, input().rstrip().split()))
    if i == 0:
        # dp 변수 초기화
        for j in range(3):
            mins[j] = scores[j]
            maxs[j] = scores[j]
    else:
        # 최소 비용 갱신
        temp_min = [mins[i] for i in range(3)]

        temp_min[0] = min(mins[0] + scores[0], mins[1] + scores[0])
        temp_min[1] = min(mins[0] + scores[1], mins[1] +
                          scores[1], mins[2] + scores[1])
        temp_min[2] = min(mins[1] + scores[2], mins[2] + scores[2])

        # 최대 비용 갱신
        temp_max = [maxs[i] for i in range(3)]
        temp_max[0] = max(maxs[0] + scores[0], maxs[1] + scores[0])
        temp_max[1] = max(maxs[0] + scores[1], maxs[1] +
                          scores[1], maxs[2] + scores[1])
        temp_max[2] = max(maxs[1] + scores[2], maxs[2] + scores[2])

        mins, maxs = temp_min, temp_max

max_val = max(maxs)
min_val = min(mins)

print(max_val, min_val)
