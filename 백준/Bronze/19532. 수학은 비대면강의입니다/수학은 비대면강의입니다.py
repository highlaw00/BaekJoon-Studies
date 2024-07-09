# ax + by = c
# dx + ey = f

# 각칸에는 -999 ~ 999 까지의 수자만 입력
# x, y가 유일하게 존재함

a, b, c, d, e, f = map(int, input().split())
flag = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            ans_x = x
            ans_y = y
            flag = True
            break
    if flag: 
        break

print(ans_x, ans_y)