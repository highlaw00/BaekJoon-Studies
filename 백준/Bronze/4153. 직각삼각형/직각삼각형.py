import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().rstrip().split()))
    nums.sort()
    a, b, c = nums
    if not a and not b and not c:
        break
    if c * c == a * a + b * b:
        print('right')
    else:
        print('wrong')
