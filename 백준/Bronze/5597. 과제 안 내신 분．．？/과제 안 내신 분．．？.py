checkList = [0 for _ in range(30)]
l = []
for i in range(28):
    n = int(input())
    l.append(n)
# 28명 입력 받음

for i in range(28):
    currNum = l[i]
    checkList[currNum - 1] += 1
# 제출한 학생의 checkList[idx] 는 1을 더해줌

l2 = []
for i in range(30):
    if checkList[i] == 0:
       l2.append(i+1) 
# checkList를 순회하며 0인 값을 2개 찾고 서로 비교 후 출력     

n1 = l2[0]
n2 = l2[1]

if n1 > n2:
    print(n2)
    print(n1)
else:
    print(n1)
    print(n2)