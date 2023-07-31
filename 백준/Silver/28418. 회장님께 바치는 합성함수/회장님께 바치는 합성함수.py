a, b, c = map(int, input().split())
d, e = map(int, input().split())

# 2차 => 판별식 사용
# 1차 => 무조건 1개만
# 상수 => 0인 경우에 무한대

t1 = a*d**2 - a*d
t2 = 2*a*d*e
t3 = a*e**2 + b*e + c - c*d - e

# 2차인 경우
if t1 != 0:
    determine = (a*d*e) ** 2 - (a*(d**2) - a * d) * \
        (a*(e**2) + b*e + c - c * d - e)
    if determine > 0:
        print("Go ahead")
    elif determine == 0:
        print("Remember my character")
    else:
        print("Head on")
# 1차
elif t2 != 0:
    print("Remember my character")
# 상수
else:
    if t3 == 0:
        print("Nice")
    else:
        print("Head on")
