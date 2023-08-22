# 좋다 -> 어떤 수 k가 다른 수 두 개의 합으로 나타낼 수 있는 경우
# 단, 위치가 다르면 무조건 다른 수 !!!
# 1 1 0 => 좋은 수의 개수가 2개

# N개의 수를 받고, N개의 수를 저장한 집합을 순회하며 다음과 같은 식을 만족하는 b를 찾는다
# k = a + b
# N개의 수 중 수의 위치가 다른 경우 값이 같아도 다른 수로 취급한다

# 1) a와 b가 다른 경우
# -> 단순히 b를 찾는다. 있다면 좋다

# 2) a와 b가 같은 경우
# -> b가 2개 이상이면 좋다

# 3) a가 0인 경우
# -> b는 k가 되니 좋다
import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().rstrip().split()))
d = dict()

for num in l:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

cnt = 0
# 리스트 순회하며 딕셔너리 참조
for i, num1 in enumerate(l):
    for j, num2 in enumerate(l):
        # 같은 수(같은 위치)라면 볼 필요 없음
        if i == j:
            continue
        num3 = num1 - num2
        if num3 in d:
            if num1 == num2 == num3:
                if d[num1] >= 3:
                    cnt += 1
                    break
            elif num2 == num3:
                if d[num2] >= 2:
                    cnt += 1
                    break
            elif num2 == 0:
                if d[num3] >= 2:
                    cnt += 1
                    break
            elif num3 == 0:
                if d[num2] >= 2:
                    cnt += 1
                    break
            else:
                cnt += 1
                break

print(cnt)
