# 종말의 수란 6이 적어도 3개이상 연속으로 들어가는 수
# 제일 작은 종말의 수는 666이며 1666, 2666, 3666, ... 이렇게 됨
# n번째로 작은 종말의 수를 구하라

n = int(input())

arr = []
streak = 0
i = 665

while len(arr) <= 10000:
    streak = 0
    i += 1
    temp_i = i
    while temp_i != 0:
        curr = temp_i % 10
        temp_i = temp_i // 10
        if curr == 6:
            streak += 1
        else:
            streak = 0

        if streak == 3:
            arr.append(i)
            streak = 0
            break

print(arr[n-1])
