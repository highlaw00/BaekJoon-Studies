input = __import__('sys').stdin.readline
n = int(input())
cnt = 0

for i in range(n):
    curr = int(input())
    if i != n - 1:
        cnt += curr - 1    
    else:
        cnt += curr
        
print(cnt)