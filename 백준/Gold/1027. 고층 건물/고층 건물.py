# 두 건물을 선택하고 두 건물을 잇는 기울기
# 두 건물 사이에 존재하는 건물과 두 건물 중 더 큰 건물과의 기울기
# 두 기울기를 비교하는데, 만약 사이에 존재하는 건물의 기울기의 절대값이 더 크다면
# 지나지 않는 것이고, 같거나 작으면 지나거나 접하는 것이다
# 이어질 수 있다면 그 건물에서 볼 수 있는 건물의 수를 +1 한다

n = int(input())
buildings = [0] + list(map(int, input().split()))
ans = 0

# i = 첫번째 건물
for i in range(1, n+1):
    # 첫번째 건물에서 보이는 건물의 수의 총 합
    total_cnt = 0
    # j = 두번째 건물
    for j in range(1, n+1):
        if i == j:
            continue
        # # 만약 첫번째 건물이 두번째 건물보다 작다면 pass
        # if buildings[i] < buildings[j]:
        #     continue

        # 첫번째 건물과 두번째 건물을 잇는 선분의 기울기를 구합니다
        # 기울기를 먼저 구합니다
        # grad = (f(i) - f(j)) / (i - j)
        grad = (buildings[i] - buildings[j]) / (i - j)

        start = i + 1 if i < j else j + 1
        end = j if i < j else i
        is_visible = True
        for k in range(start, end):
            # k점부터 end까지의 기울기와
            # 기존의 기울기를 비교합니다
            # 기존 기울기가 없는 경우

            temp_grad = (buildings[k] - buildings[end]) / (k - end)

            # 기존 기울기가 0인 경우
            if grad == 0:
                # k와 end의 높이를 비교합니다
                # 만약 end보다 크거나 같으면 false
                if buildings[k] >= buildings[end]:
                    is_visible = False
                    break
            else:
                # 새로운 기울기가 작거나 같으면 false
                if temp_grad <= grad:
                    is_visible = False
                    break
        if is_visible:
            total_cnt += 1

    ans = max(ans, total_cnt)

print(ans)
