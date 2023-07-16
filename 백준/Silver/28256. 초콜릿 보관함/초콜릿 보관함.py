# 주어진 리스트와 초콜릿의 분포가 일치하는지 판단하는 프로그램
# 1. DFS를 모든 인덱스에 대해 진행(가운데 인덱스 제외)
# 2. DFS 진행하며 연결된 초콜릿 기록 (재귀 시작 시 리스트 전달하여 재귀 진행시 인덱스 삽입)
# 3. 2번에서 전달한 리스트와 주어진 리스트를 대조

t = int(input())
# 하우상좌
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def in_range(i, j):
    return 0 <= i and i < 3 and 0 <= j and j < 3


def dfs(i, j):
    # 방문하면 이어진 초콜릿의 길이를 + 1
    global cnt
    cnt += 1
    # 인접한 칸을 순회하며 ...
    # -, X, 이미 방문했으면 무시
    # 초콜릿이 존재하면 순회
    for di, dj in dirs:
        new_i, new_j = i + di, j + dj
        global visited
        if in_range(new_i, new_j) and not visited[new_i][new_j] and mat[new_i][new_j] == 'O':
            visited[new_i][new_j] = 1
            dfs(new_i, new_j)
    return


for _ in range(t):
    mat = [list(input()) for _ in range(3)]
    visited = [[0 for _ in range(3)] for _ in range(3)]
    l = list(map(int, input().split()))
    n = l[0]
    l = l[1:]
    arr = []

    for i in range(3):
        for j in range(3):
            if not visited[i][j] and mat[i][j] == 'O':
                cnt = 0
                visited[i][j] = 1
                dfs(i, j)
                arr.append(cnt)

    arr.sort()
    isDifferent = False
    if n != len(arr):
        print(0)
    else:
        for i in range(n):
            if l[i] != arr[i]:
                print(0)
                isDifferent = True
                break
        if not isDifferent:
            print(1)
