def is_biggest_size(k, prefix):
    # 가로 세로 길이가 n인 정사각형의 존재 여부를 반환합니다.
    n = len(prefix)
    m = len(prefix[0])
    
    for i in range(n-k+1):
        for j in range(m-k+1):
            if i == 0 and j == 0:
                summ = prefix[i+k-1][j+k-1]
            elif i == 0 and j != 0:
                summ = prefix[i+k-1][j+k-1] - prefix[i+k-1][j-1]
            elif i != 0 and j == 0:
                summ = prefix[i+k-1][j+k-1] - prefix[i-1][j+k-1]
            else:
                summ = prefix[i+k-1][j+k-1] - prefix[i-1][j+k-1] - prefix[i+k-1][j-1] + prefix[i-1][j-1]
            
            if summ == k * k:
                return True
    
    return False
    

def solution(board):
    n = len(board) # 행 개수
    m = len(board[0]) # 열 개수
    
    prefix = [[0 for _ in range(m)] for _ in range(n)]
    
    # 최상단 행 초기화
    for i in range(m):
        prefix[0][i] = board[0][i]   
        if i != 0:
            prefix[0][i] += prefix[0][i-1]
    # 최좌단 열 초기화
    for i in range(n):
        prefix[i][0] = board[i][0]
        if i != 0:
            prefix[i][0] += prefix[i-1][0]
    
    for i in range(1, n):
        for j in range(1, m):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + board[i][j]
    
    # 가장 큰 정사각형의 가로, 세로 길이를 찾습니다.
    answer = 0
    for i in range(min(n, m), 0, -1):
        if is_biggest_size(i, prefix):
            answer = i * i
            break
    
    return answer