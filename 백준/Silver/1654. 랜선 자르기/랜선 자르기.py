# array: 랜 길이 배열, length: 자를 랜선의 길이, taget_amt: 만들어야하는 개수
def isAble(array, length, target_amt):
    cnt = 0
    for lan in array:
        cnt += lan // length
    return cnt >= target_amt

k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)
answer = 0

while left <= right:
    mid = (left + right) // 2
    # mid 길이의 랜선 N개 이상을 만들 수 있다면?
    # 정답 갱신 후, left = mid + 1
    if isAble(lans, mid, n):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)