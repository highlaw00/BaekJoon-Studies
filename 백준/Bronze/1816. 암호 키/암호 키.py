# 매우 큰 소수의 기준을 10^6보다 큰 소수라고 정하자.
# 어떤수 S가 주어졌을 때, 이 수가 적절한 암호 키인지 아닌지를 확인하라
# 만약 S의 모든 소인수가 10^6보다 크다면 그 수는 적절한 암호 키이다.

n = int(input())

for _ in range(n):
    s = int(input())
    isSuited = True
    for i in range(2, 1000000):
        if s % i == 0:
            isSuited = False
            break
    if isSuited:
        print("YES")
    else:
        print("NO")
