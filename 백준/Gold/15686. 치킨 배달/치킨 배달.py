import sys
INF = sys.maxsize

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = INF

# 백트래킹으로 살려둘 m개의 치킨집 개수를 고른다.
# 각 집에서 m개의 치킨집과의 거리를 측정한다. <- 메모이제이션
# dist[(i,j)] = [(i_1,j_1): 1, (i_2,j_2): 2, ...]
# 위 처럼 각 집에서 모든 치킨집과의 거리를 기록해둔다.
houses = []
chickens = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      houses.append((i, j))
    elif board[i][j] == 2:
      chickens.append((i, j))

house_to_chicken_dist = dict()
for i_h, j_h in houses:
  house_to_chicken_dist[(i_h), (j_h)] = dict()
  dists = house_to_chicken_dist[(i_h), (j_h)]
  for i_c, j_c in chickens:
    dists[(i_c,j_c)] = abs(i_h-i_c) + abs(j_h-j_c)

# stack: 폐업되지 않을 치킨집 좌표
def back(stack, k):
  if len(stack) == m:
    total_dist = 0
    for i_h, j_h in houses:
      min_dist = INF
      dists = house_to_chicken_dist[(i_h, j_h)]
      for i_c, j_c in stack:
        min_dist = min(min_dist, dists[(i_c,j_c)])
      total_dist += min_dist
    global answer
    answer = min(answer, total_dist)
    return
  for i in range(k, len(chickens)):
    chicken = chickens[i]
    stack.append(chicken)
    back(stack, i+1)
    stack.pop()

back([], 0)
print(answer)