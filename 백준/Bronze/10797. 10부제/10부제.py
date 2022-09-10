date = int(input())
n1, n2, n3, n4, n5 = map(int,input().split())
cnt = 0

if n1 == date:
    cnt += 1 
if n2 == date:
    cnt += 1
if n3 == date:
    cnt += 1
if n4 == date:
    cnt +=1
if n5 == date:
    cnt +=1

print(cnt)