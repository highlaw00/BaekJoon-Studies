s = ''

while True:
    try:
        line = input()
        s += line
    except EOFError:
        break

l = [0 for i in range(26)]
for letter in s:
    if letter == ' ':
        continue
    idx = ord(letter) - ord('a')
    l[idx] += 1

max_val = max(l)

for i in range(26):
    if l[i] == max_val:
        print(chr(i + ord('a')), end='')
print()
