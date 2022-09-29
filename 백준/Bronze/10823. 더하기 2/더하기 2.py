s = ''
while True:
    try:
        line = input()
        s += line
    except EOFError:
        break

l = list(s.split(','))
sum = 0
for n in l:
    sum += int(n)
print(sum)