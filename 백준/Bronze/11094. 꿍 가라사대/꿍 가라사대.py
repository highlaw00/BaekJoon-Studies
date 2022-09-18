n = int(input())
for i in range(n):
    string = input()
    if string[:10] == "Simon says":
        print(string[10:])
    else:
        continue