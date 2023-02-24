word = input()
ans = ""

for char in word:
    # A, B, C인 경우
    if "A" <= char <= "C":
        ans += chr(ord(char) + 23)
    # A, B, C가 아닌 경우
    else:
        ans += chr(ord(char) - 3)

print(ans)
