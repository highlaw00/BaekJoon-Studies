def get_available_snack_amount(snack_lengths, l):
    cnt = 0
    for snack_length in snack_lengths:
        max_snack_cnt = snack_length // l # 하나의 과자에서 l만큼의 길이를 가지는 과자의 개수
        cnt += max_snack_cnt
    return cnt

m, n = map(int, input().split())
lens = list(map(int, input().split())) # 오름차순 정렬되어있다

# 과자의 길이(l) 결정
# 길이 l의 과자를 m개 만들 수 있는지 확인
# 만약 부족하다면 과자의 길이를 줄인다.
# 만약 그것보다 많이 만들수있으면 과자의 길이를 늘린다.
# m개 이상의 과자를 만들 수 있고 그 중 가장 큰 l값을 찾는것
# 

left = 1
right = max(lens)
ans = 0

while left <= right:
    mid = (left + right) // 2

    snack_amt = get_available_snack_amount(lens, mid)
    # m개 이상 만들수 있는 경우 과자 길이는 (mid + 1, right)
    if snack_amt >= m:
        ans = max(ans, mid)
        left = mid + 1
    # m개를 만들지 못하는 경우 과자 길이는 (left, mid - 1)
    else:
        right = mid - 1

print(ans)