# n이 주어졌을 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램
# 루트n부터 확인
# 하나의 제곱수 => n이 제곱수인 경우
import math

n = int(input())

sq_lis = [i * i for i in range(1, int(math.sqrt(n) + 1))]
sq_lis.reverse()

# 1개인지 확인
if sq_lis[0] == n:
    print(1)
    exit()

# 2개인지 확인
for i in range(len(sq_lis)):
    for j in range(i, len(sq_lis)):
        if sq_lis[i] + sq_lis[j] == n:
            print(2)
            exit()

# 3개인지 확인
for i in range(len(sq_lis)):
    for j in range(i, len(sq_lis)):
        for k in range(i, len(sq_lis)):
            if sq_lis[i] + sq_lis[j] + sq_lis[k] == n:
                print(3)
                exit()

# 4개인지 확인
for i in range(len(sq_lis)):
    for j in range(i, len(sq_lis)):
        for k in range(i, len(sq_lis)):
            for m in range(i, len(sq_lis)):
                if sq_lis[i] + sq_lis[j] + sq_lis[k] + sq_lis[m] == n:
                    print(4)
                    exit()
