n = int(input())
pow2 = [2 ** x for x in range(65)]
pow2.reverse()
num = n
flag = False

for i in range(65):
    for j in range(65):
        gap = abs(num - pow2[j])
        if gap == 1:
            flag = True
            key = 64 - j
            break
    num = num // 2
    if flag:
        break
    
if n == 2 ** 63:
    print(1)
else:
    print(key)