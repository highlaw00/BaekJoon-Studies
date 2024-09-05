def char_to_index(char):
    col = char[0]
    row = char[1]
    new_row = 8 - int(row)
    new_col = ord(col) - ord('A')
    return (new_row, new_col)

def index_to_char(i, j):
    new_row = 8 - i
    new_col = chr(ord('A') + j)
    return new_col + str(new_row)
    

def invalid(i, j):
    return i < 0 or j < 0 or i >= 8 or j >= 8

EMPTY = 0
KING = 1
STONE = 2
board = [[EMPTY for _ in range(8)] for _ in range(8)]
moves = {
    'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
    'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)
}

king_info, stone_info, n = input().split()
king_i, king_j = char_to_index(king_info)
stone_i, stone_j = char_to_index(stone_info)

for _ in range(int(n)):
    command = input()
    di, dj = moves[command]
    # 이동 가능성 확인
    king_ni, king_nj = king_i + di, king_j + dj
    if invalid(king_ni, king_nj):
        continue
    
    # 돌 유무 확인. 있으면 돌 먼저 이동
    if stone_i == king_ni and stone_j == king_nj:
        # 돌의 이동 가능성 확인
        stone_ni, stone_nj = stone_i + di, stone_j + dj
        if invalid(stone_ni, stone_nj):
            continue
        # 돌 이동
        stone_i, stone_j = stone_ni, stone_nj
    
    # 킹 이동
    king_i, king_j = king_ni, king_nj

king_loc = index_to_char(king_i, king_j)
stone_loc = index_to_char(stone_i, stone_j)
print(king_loc)
print(stone_loc)