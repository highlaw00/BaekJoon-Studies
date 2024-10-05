import sys
CHECKED = sys.maxsize

board = [list(map(int, input().split())) for _ in range(5)]
answers = []
for _ in range(5):
    line = list(map(int, input().split()))
    for num in line:
        answers.append(num)

def check_bingo(board):
    bingo_cnt = 0
    for i in range(5):
        # 행 확인
        checked_cnt = 0
        for j in range(5):
            if board[i][j] == CHECKED:
                checked_cnt += 1
        if checked_cnt == 5:
            bingo_cnt += 1
            
        # 열 확인
        checked_cnt = 0
        for j in range(5):
            if board[j][i] == CHECKED:
                checked_cnt += 1
        if checked_cnt == 5:
            bingo_cnt += 1
    
    # 우하향 대각 확인
    checked_cnt = 0
    for i in range(5):
        if board[i][i] == CHECKED:
            checked_cnt += 1
    if checked_cnt == 5:
        bingo_cnt += 1
    # 우상향 대각 확인
    checked_cnt = 0
    for i in range(5):
        if board[4-i][i] == CHECKED:
            checked_cnt += 1
    if checked_cnt == 5:
        bingo_cnt += 1
    
    if bingo_cnt >= 3:
        return True
    return False

for idx, num in enumerate(answers):
    target_i, target_j = 0, 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                target_i, target_j = i, j
                break
    board[target_i][target_j] = CHECKED
    if check_bingo(board):
        print(idx+1)
        break