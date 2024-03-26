import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))
ans = [li[0], li[1], li[2]]
minVal = sys.maxsize

for fixed in range(0, n-2):
    # 숫자 하나를 고정시키고 투포인터를 사용해 정답 찾기
    left, right = fixed + 1, n-1
    
    while left != right:
        summation = li[fixed] + li[left] + li[right]
        # 세 용액의 합이 정답인지 확인 및 갱신
        if minVal > abs(summation):
            minVal = abs(summation)
            ans = [li[fixed], li[left], li[right]]
        
        # 세 용액을 더한 값이 양수라면: 오른쪽을 왼쪽으로 당김
        if summation > 0:
            right -= 1
        # 세 용액을 더한 값이 음수라면: 왼쪽을 오른쪽으로 밂
        elif summation < 0:
            left += 1
        else: break

print(' '.join(map(str, ans)))