import sys
import math
input = sys.stdin.readline
n, q = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
d = dict()


for i, elem in enumerate(a):
    if elem in d:
        d[elem].append(i)
    else:
        d[elem] = [i]

for _ in range(q):
    cmd, num = map(int, input().rstrip().split())

    if cmd == 1:
        # 0이라면 d[0] 확인
        if num == 0:
            if 0 in d and len(d[0]) >= 1:
                print(1)
            else:
                print(0)
            continue
        # 약수가 2개 이상 존재하면 1 출력
        flag = False
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if i != num // i:
                    n1, n2 = i, num // i
                    if n1 in d and n2 in d and len(d[n1]) >= 1 and len(d[n2]) >= 1:
                        flag = True
                else:
                    n1 = i
                    if n1 in d and len(d[n1]) >= 2:
                        flag = True
        if flag:
            print(1)
        else:
            print(0)
    else:
        if num-1 in d[a[num-1]]:
            d[a[num-1]].remove(num-1)
        if 0 in d:
            d[0].append(num-1)
        else:
            d[0] = [num-1]
