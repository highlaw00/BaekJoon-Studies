import sys

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
houses = []
chickens = []
dists = []

for i in range(n):
    for j in range(n):
        info = mat[i][j]
        # 모든 집의 인덱스를 저장합니다.
        if info == 1:
            houses.append((i, j))
        elif info == 2:
            chickens.append((i, j))

for (x, y) in houses:
    # 모든 집에 대해 각 치킨 집에 대한 치킨 거리를 구합니다.
    each_dist = []
    for (c_x, c_y) in chickens:
        # 치킨집의 거리를 계산한 후 dists에 삽입합니다.
        dist = abs(x-c_x) + abs(y-c_y)
        each_dist.append(dist)
    dists.append(each_dist)

ans = sys.maxsize
stack = []
# 백트래킹 과정을 최대 m번 거치며 최소 도시의 치킨 거리를 구합니다.


def get_city_score(indices):
    # indices에 있는 idx번 째 열을 제외한 행렬에서 각 행의 최소 값을 모두 더합니다.
    city_score = 0
    for row in dists:
        minimum = sys.maxsize
        for i in range(len(row)):
            if i in indices and row[i] < minimum:
                minimum = row[i]
        city_score += minimum

    return city_score


def backtrack(idx, cnt):
    # 기저 사례
    if cnt == m:
        return
    for i in range(idx, len(chickens)):
        stack.append(i)
        # stack에 존재하는 치킨집만 남기고 모두 폐업 합니다.
        # 그 때의 치킨 거리를 구합니다.
        city_score = get_city_score(stack)
        global ans
        if ans > city_score:
            ans = city_score
        backtrack(i + 1, cnt + 1)
        stack.pop()


backtrack(0, 0)
print(ans)
