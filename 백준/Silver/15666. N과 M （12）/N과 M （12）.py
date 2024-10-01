n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []
printed = set()

def back(k):
    # base condition
    if len(s) == m:
        string = ' '.join(map(str, s))
        if string not in printed:
            print(string)
            printed.add(string)
        return
    
    for i in range(k, len(numbers)):
        num = numbers[i]
        s.append(num)
        back(i)
        s.pop()
    
back(0)