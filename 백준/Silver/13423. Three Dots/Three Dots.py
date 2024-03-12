import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    dots = list(map(int, input().split()))
    dots.sort()
    
    dicts = dict()
    for num in dots:
        dicts[num] = True
        
    ans = 0
    for i in range(len(dots) - 1):
        for j in range(i+1, len(dots)):
            num1 = dots[i]
            num2 = dots[j]
            gap = num2 - num1
            if (num2 + gap) in dicts:
                ans += 1
    
    print(ans)