import math

k = int(input())
# 총 무게를 k만큼 가져오고 싶다
# 단, 무게는 2 이상이며, 종류에는 제한이 없다.
arr = []
cnt = 0

for i in range(2, int(math.sqrt(k)) + 1):
    while k % i == 0:
        cnt += 1
        k //= i
        arr.append(i)

if k != 1:
    cnt += 1
    arr.append(k)

print(cnt)
for elem in arr:
    print(elem, end=" ")
