import sys
input = sys.stdin.readline

n = int(input().rstrip())
students = []
likes = [dict() for _ in range(n*n + 1)]
grid = [[0 for _ in range(n)] for _ in range(n)]
dirs = ((0, -1), (0, 1), (1, 0), (-1, 0))

for i in range(n*n):
    line = list(map(int, input().rstrip().split()))
    student_number = line[0]
    students.append(student_number)
    likes[student_number] = line[1:]


def check_first_condition(student_number):
    # 비어있는 모든 칸 확인.
    # 해당 칸에 인접한 좋아하는 학생 수 조사
    cnt = 0
    max_val = 0
    student_likes = likes[student_number]
    candidates = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            # 인접한 학생 수 조사
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                if grid[ni][nj] in student_likes:
                    cnt += 1
            # 인접한 학생 수 기록
            candidates[i][j] = cnt
            # 최대 인접 학생 수 갱신
            max_val = max(cnt, max_val)
            cnt = 0

    ret = []
    for i in range(n):
        for j in range(n):
            if candidates[i][j] == max_val and grid[i][j] == 0:
                ret.append((i, j))
    return ret


def check_second_condition(seats):
    # 인접한 칸중에서 비어있는 칸이 가장 많은 칸으로 자리를 정함
    candidates = [[0 for _ in range(n)] for _ in range(n)]
    max_val = 0

    for i, j in seats:
        cnt = 0
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if grid[ni][nj] == 0:
                cnt += 1
        max_val = max(max_val, cnt)
        candidates[i][j] = cnt

    ret = []
    for i, j in seats:
        if candidates[i][j] == max_val:
            ret.append((i, j))

    return ret


def get_satisfying_point():
    ret = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            student_num = grid[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                if grid[ni][nj] in likes[student_num]:
                    cnt += 1
            if cnt == 0:
                continue
            ret += int(10 ** (cnt-1))
    return ret


for student_num in students:
    candidates = check_first_condition(student_num)
    if len(candidates) == 1:
        i, j = candidates[0]
        grid[i][j] = student_num
        continue

    candidates = check_second_condition(candidates)
    i, j = candidates[0]
    grid[i][j] = student_num

print(get_satisfying_point())
