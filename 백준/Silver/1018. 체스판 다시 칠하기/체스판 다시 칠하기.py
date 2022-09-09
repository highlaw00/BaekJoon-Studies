n, m = map(int, input().split())

array = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
    string = list(input())
    for j in range(m):
        array[i][j] = string[j]

# 8*8 체스판이 주어지면 [0][0]이 각각 B,W일때 몇 번 칠해야하는지
# 카운트 하는 코드

max_col_start = n - 8
max_row_start = m - 8
c = 'W'

min_cnt = 64

for k in range(0, max_col_start+1):
    for l in range(0, max_row_start + 1):
        w_cnt = 0
        b_cnt = 0
        for i in range(k, k+8):
            if (i % 2 == 0):
                c = 'W'
            else:
                c = 'B'
            for j in range(l, l+8):
                if (array[i][j] != c):
                    w_cnt += 1
                if (c == 'W'):
                    c = 'B'
                else:
                    c = 'W'

        for i in range(k, k+8):
            if (i % 2 == 0):
                c = 'B'
            else:
                c = 'W'
            for j in range(l, l+8):
                if (array[i][j] != c):
                    b_cnt += 1
                if (c == 'W'):
                    c = 'B'
                else:
                    c = 'W'
        if (min_cnt > w_cnt):
            min_cnt = w_cnt
        if (min_cnt > b_cnt):
            min_cnt = b_cnt

print(min_cnt)
