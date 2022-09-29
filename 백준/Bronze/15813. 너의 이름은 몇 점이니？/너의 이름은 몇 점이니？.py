n = int(input())
name = input()
sum = 0
for c in name:
    sum += ord(c) - 64
print(sum)
