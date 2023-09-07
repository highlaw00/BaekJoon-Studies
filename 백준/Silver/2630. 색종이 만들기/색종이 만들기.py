import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
white, blue = 0, 0


def check_equality(s, e):
    s_i, s_j = s
    e_i, e_j = e
    base_color = grid[s_i][s_j]
    for i in range(s_i, e_i + 1):
        for j in range(s_j, e_j + 1):
            if base_color != grid[i][j]:
                return -1
    return base_color


def get_papers(s, e):
    s_i, s_j = s
    e_i, e_j = e
    global blue, white

    # 전체 면적 확인
    res = check_equality(s, e)
    if res != -1:
        if res:
            blue += 1
        else:
            white += 1
        return

    # 2사분면 시작 지점
    s_i_2, s_j_2 = s_i, s_j
    # 2사분면 끝 지점
    e_i_2, e_j_2 = (s_i + e_i) // 2, (s_j + e_j) // 2
    # 1사분면 시작 지점
    s_i_1, s_j_1 = s_i, e_j_2 + 1
    # 1사분면 끝 지점
    e_i_1, e_j_1 = (s_i + e_i) // 2, e_j
    # 3사분면 시작 지점
    s_i_3, s_j_3 = (s_i + e_i) // 2 + 1, s_j
    # 3사분면 끝 지점
    e_i_3, e_j_3 = e_i, e_j_2
    # 4사분면 시작 지점
    s_i_4, s_j_4 = (s_i + e_i) // 2 + 1, (s_j + e_j) // 2 + 1
    # 4사분면 끝 지점
    e_i_4, e_j_4 = e_i, e_j

    starts = [
        (s_i_2, s_j_2),
        (s_i_1, s_j_1),
        (s_i_3, s_j_3),
        (s_i_4, s_j_4)
    ]
    ends = [
        (e_i_2, e_j_2),
        (e_i_1, e_j_1),
        (e_i_3, e_j_3),
        (e_i_4, e_j_4)
    ]

    for start, end in zip(starts, ends):
        res = check_equality(start, end)
        if res == -1:
            get_papers(start, end)
        else:
            color = res
            if color:
                blue += 1
            else:
                white += 1


get_papers((0, 0), (n-1, n-1))
print(white, blue, sep="\n")
