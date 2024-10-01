n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
used = [False for _ in range(len(numbers))]
printed = set()
s = []

def back():
    if len(s) == m:
        string = ' '.join(map(str, s))
        if string not in printed:
            print(string)
            printed.add(string)
        return
    for i in range(len(numbers)):
        if used[i]:
            continue
        num = numbers[i]
        s.append(num)
        used[i] = True
        back()
        used[i] = False
        s.pop()

back()