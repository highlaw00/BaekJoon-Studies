n, m = map(int,input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def back(k):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(k, len(numbers)):
        num = numbers[i]
        s.append(num)
        back(i)
        s.pop()

back(0)