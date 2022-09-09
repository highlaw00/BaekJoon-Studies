import sys

n = int(input())
max_margin = -sys.maxsize - 1
max_margin_cost = 0

total_list = []

for i in range(0, n):
    l = list(map(int, input().split()))
    total_list.append(l)

for curr_cost in total_list:
    # total_list의 원소 중 금액을 순회하는 for loop
    std_cost = curr_cost[0]
    margin_sum = 0
    for total_list_it in total_list:
        # cost와 total_list에 있는 모든 원소와
        # 마진을 계산하기 위한 loop
        cmp_cost = total_list_it[0]
        cmp_del_cost = total_list_it[1]
        if (std_cost == cmp_cost):
            curr_margin = cmp_cost - cmp_del_cost
            if (curr_margin <= 0):
                continue
            else:
                margin_sum += curr_margin
        elif (std_cost < cmp_cost):
            curr_margin = std_cost - cmp_del_cost
            if (curr_margin <= 0):
                continue
            else:
                margin_sum += curr_margin
    if (max_margin == margin_sum and max_margin_cost > std_cost):
        max_margin_cost = std_cost
    elif (max_margin < margin_sum):
        max_margin = margin_sum
        max_margin_cost = std_cost


if (max_margin <= 0):
    print(0)
else:
    print(max_margin_cost)
