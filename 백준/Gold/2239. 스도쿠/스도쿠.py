board = [list(map(int,input())) for _ in range(9)]
# 행 집합
row_sets = [set() for _ in range(9)]
# 열 집합
col_sets = [set() for _ in range(9)]
# 3*3 집합
mat_sets = [[set() for _ in range(3)] for _ in range(3)]
zeros = []
printed = False

for i in range(9):
  for j in range(9):
    num = board[i][j]
    if num != 0:
      row_sets[i].add(num)
      col_sets[j].add(num)
      mat_sets[i//3][j//3].add(num)
    else:
      zeros.append((i,j))

def back(cnt):
  if cnt == len(zeros):
    for row in board:
      print(''.join(map(str, row)))
    return True
  row, col = zeros[cnt]
  for num in range(1, 10):
    if (num not in row_sets[row]) and \
       (num not in col_sets[col]) and \
       (num not in mat_sets[row//3][col//3]):
      # row, col 자리에 num 삽입
      board[row][col] = num
      row_sets[row].add(num)
      col_sets[col].add(num)
      mat_sets[row//3][col//3].add(num)
      result = back(cnt+1)
      if result:
        return True
      mat_sets[row//3][col//3].remove(num)
      col_sets[col].remove(num)
      row_sets[row].remove(num)
      board[row][col] = 0

back(0)