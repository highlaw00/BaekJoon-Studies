line = input()
ans = [0 for _ in range(len(line)*3)]

for i, digit in enumerate(line):
    x = int(digit)
    partial = [0, 0, 0]
    for j, num in enumerate((4, 2, 1)):
        partial[j] = str(x // num)
        x = x % num
    ans_idx = i * 3
    ans[ans_idx] = partial[0]
    ans[ans_idx + 1] = partial[1]
    ans[ans_idx + 2] = partial[2]

start_idx = 2
for i in range(3):
    if ans[i] == '1':
        start_idx = i
        break
for i in range(start_idx, len(ans)):
    print(ans[i], end='')
