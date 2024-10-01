n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
printed = set()
s = []

def back(k):
    if len(s) == m:
        string = ' '.join(map(str, s))
        if string not in printed:
            print(string)
            printed.add(string)
        return
    for i in range(k, len(numbers)):
        number = numbers[i]
        s.append(number)
        back(i+1)
        s.pop()

back(0)