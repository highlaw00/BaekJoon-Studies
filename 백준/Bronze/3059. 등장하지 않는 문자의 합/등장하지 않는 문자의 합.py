t = int(input())
l = [chr(65 + i) for i in range(26)]

for _ in range(t):
    string = input()
    s = set()
    sum = 0
    for letter in string:
        s.add(letter)
    for letter in l:
        if letter not in s:
            sum += ord(letter)
    print(sum)