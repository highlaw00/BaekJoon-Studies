encrypted = input()
alphabets = [chr(ch) for ch in range(ord('A'), ord('Z') + 1)]
ans = ['' for _ in range(len(encrypted))]

for i, ch in enumerate(encrypted):
    decrypted_ch = ((ord(ch) - ord('A')) - 3) % 26
    decrypted_ch = alphabets[decrypted_ch]
    ans[i] = decrypted_ch

print(''.join(ans))
