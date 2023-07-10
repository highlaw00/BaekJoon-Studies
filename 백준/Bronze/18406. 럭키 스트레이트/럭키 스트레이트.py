n = input()
left, right = n[:len(n) // 2], n[len(n) // 2:]
left_sum, right_sum = 0, 0

for num in left:
    num = int(num)
    left_sum += num

for num in right:
    num = int(num)
    right_sum += num

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
