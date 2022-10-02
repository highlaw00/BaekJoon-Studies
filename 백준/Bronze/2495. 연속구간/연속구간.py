# 연속되는 숫자가 없으면 1을 출력
# 연속되는 숫자가 있다면 가장 긴 것의 길이를 출력

for i in range(3):
    len = 0
    max = 0
    s = input()
    last = s[0]
    for j in s:
        if j == last:
            len += 1
            if len > max:
                max = len
        else:
            len = 1
        last = j
    print(max)


