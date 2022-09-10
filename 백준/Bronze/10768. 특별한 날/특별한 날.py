m = int(input())
d = int(input())

if m < 2:
    # 월이 1월인 경우
    print("Before")
elif m > 2:
    # 월이 3월 이상일 경우
    print("After")
else:
    if d == 18:
        print("Special")
    elif d > 18:
        print("After")
    else:
        print("Before")