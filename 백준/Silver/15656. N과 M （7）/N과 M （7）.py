n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def back(cnt):
    if cnt == m:
        print(' '.join(map(str, s)))
        return
    for i in range(len(numbers)):
        num = numbers[i]
        s.append(num)
        back(cnt+1)
        s.pop()

back(0)