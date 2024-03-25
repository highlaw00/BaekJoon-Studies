n = int(input())
numbers = list(map(int, input().split()))
left, right = 0, n-1
minVal = abs(numbers[left] + numbers[right])
ans = [numbers[left], numbers[right]]

while left != right:
    # 최소 합의 절댓값 갱신
    if minVal > abs(numbers[left] + numbers[right]):
        minVal = abs(numbers[left] + numbers[right])
        ans = [numbers[left], numbers[right]]
    
    # 두 수의 합이 양수인 경우: 합이 작아져야하기에 오른쪽이 왼쪽으로 이동
    if numbers[left] + numbers[right] > 0:
        right -= 1
    # 두 수의 합이 음수인 경우: 합이 커져야하기에 왼쪽이 오른쪽으로 이동
    elif numbers[left] + numbers[right] < 0:
        left += 1
    else: break

print(' '.join(map(str, ans)))