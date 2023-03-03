board = list(list("" for _ in range(3)) for _ in range(3))

p = int(input())
winner = 0

while 1:
    # 좌표 입력
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    # 좌표에 문자 삽입
    if p == 1:
        board[x][y] = "O"
        p = 2
    elif p == 2:
        board[x][y] = "X"
        p = 1
    # 끝났는지 확인
    res = []
    # 행부터 확인하기
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != ""):
            if board[i][0] == "O":
                winner = 1
            else:
                winner = 2

    # 열부터 확인하기
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != ""):
            if board[0][i] == "O":
                winner = 1
            else:
                winner = 2

    # 대각선 확인하기
    if (board[0][0] == board[1][1] == board[2][2]) and (board[1][1] != ""):
        if board[1][1] == "O":
            winner = 1
        else:
            winner = 2

    if (board[0][2] == board[1][1] == board[2][0]) and (board[1][1] != ""):
        if board[1][1] == "O":
            winner = 1
        else:
            winner = 2

    # 승자가 판결났다면 끝내고 판결나지 않았으면 무승부 확인
    if winner != 0:
        break
    else:
        cnt = 0
        for row in board:
            for elem in row:
                if elem != "":
                    cnt += 1
        if cnt == 9:
            winner = 0
            break
print(winner)
