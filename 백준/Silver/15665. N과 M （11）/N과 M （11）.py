n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []
printed = set()

def back():
    if len(s) == m:
        string = ' '.join(map(str, s))
        if string not in printed:
            print(string)
            printed.add(string)
        return
    
    for i in range(len(numbers)):
        number = numbers[i]
        s.append(number)
        back()
        s.pop()

back()