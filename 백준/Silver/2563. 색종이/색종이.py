n = int(input())
mat = [[False for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    # x, x~10 과 y, y~10 사이에 존재하는 값을 모두 True로 만들어야함
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            mat[i][j] = True

cnt = 0
for i in range(0, 100):
    for j in range(0, 100):
        if mat[i][j]:
            cnt += 1

print(cnt)
