import sys
input = sys.stdin.readline

# n 입력
n = int(input())

# 3*n 씩 안내판 숫자
# 3*n + 1 자리에 존재하는 것은 공백임
board = [[['' for _ in range(3)] for _ in range(5)] for _ in range(n)]
answer = [[['' for _ in range(3)] for _ in range(5)] for _ in range(10)]
ref_lines = ["###...#.###.###.#.#.###.###.###.###.###",
             "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
             "#.#...#.###.###.###.###.###...#.###.###",
             "#.#...#.#.....#...#...#.#.#...#.#.#...#",
             "###...#.###.###...#.###.###...#.###.###"]

# i -> 현재 저장하려는 숫자
for i in range(10):
    for j in range(5):
        l = 0
        for k in range(i * 4, i * 4 + 3):
            answer[i][j][l] = ref_lines[j][k]
            l += 1

lines = []
# 5개의 행 입력
for _ in range(5):
    line = input().rstrip()
    lines.append(line)

for i in range(n):
    for j in range(5):
        l = 0
        for k in range(i * 4, i * 4 + 3):
            board[i][j][l] = lines[j][k]
            l += 1

# board의 전구가 꺼진 경우 -> 상관없음
# board의 전구가 켜진 경우 -> answer도 켜져있어야 함


def check_every_num(n):
    curr_board = board[n]
    ret = []
    for idx, num in enumerate(answer):
        is_able = True
        for i in range(5):
            for j in range(3):
                if curr_board[i][j] == '.':
                    continue
                if num[i][j] != '#':
                    is_able = False
                    break
        if is_able:
            ret.append(idx)

    return ret


ans = 0
available_nums_collection = []

for i in range(n):
    available_nums = check_every_num(i)
    if not available_nums:
        ans = -1
    available_nums_collection.append(available_nums)

available_nums_collection.reverse()

if ans == -1:
    print(ans)
else:
    prefix = [1 for _ in range(n)]
    dp = [0 for _ in range(n)]
    dp[0] = sum(available_nums_collection[0])
    total_cnt = len(available_nums_collection[0])
    # 길이 prefix(누적곱) 먼저 구합니다
    for i in range(1, n):
        prefix[i] = prefix[i-1] * len(available_nums_collection[i-1])
    # dp배열을 구합니다
    # i번째까지 안내판이 존재할 때, 경우의 수를 반환합니다
    for i in range(1, n):
        for j in available_nums_collection[i]:
            dp[i] += 10 ** i * j * prefix[i] + dp[i-1]
        total_cnt *= len(available_nums_collection[i])

    print(dp[n-1] / total_cnt)
