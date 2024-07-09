import sys

input = sys.stdin.readline
r, c = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
filtered_image = [[0 for _ in range(c-2)] for _ in range(r-2)]

def get_medium(matrix, start_i, start_j):
    l = []
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            l.append(matrix[i][j])
    l.sort()
    return l[4];

for i in range(0, r-2):
    for j in range(0, c-2):
        medium = get_medium(image, i, j)
        filtered_image[i][j] = medium

ans_cnt = 0
for row in filtered_image:
    for num in row:
        if num >= t: 
            ans_cnt += 1

print(ans_cnt)