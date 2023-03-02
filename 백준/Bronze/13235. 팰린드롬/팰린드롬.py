s = input()
max_idx = len(s) - 1
flag = True
for i in range(len(s) // 2):
    front_char = s[i]
    end_char = s[max_idx - i]
    if front_char != end_char:
        flag = False
        break
print("true" if flag else "false")
