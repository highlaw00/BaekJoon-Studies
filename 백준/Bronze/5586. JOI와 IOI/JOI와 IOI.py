string = input()

joi_cnt = 0
ioi_cnt = 0

for idx in range(len(string) - 2):
    if string[idx] == 'J':
        if string[idx + 1] == 'O' and string[idx + 2] == 'I':
            joi_cnt += 1
    elif string[idx] == 'I':
        if string[idx + 1] == 'O' and string[idx + 2] == 'I':
            ioi_cnt += 1

print(joi_cnt)
print(ioi_cnt)
