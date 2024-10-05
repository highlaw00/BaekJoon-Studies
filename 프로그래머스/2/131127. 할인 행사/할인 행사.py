def solution(want, number, discount):
    answer = 0
    # discount를 10개 단위로 0부터 len(discount) - 10까지 확인해나간다.
    # 해당 부분 discount를 순회하면서 want,number를 만족하는지 확인한다.
    want_number = {want[i]: number[i] for i in range(len(want))}
    
    buyable = {}
    # 처음 10일 살 수 있는 것 기록
    for i in range(10):
        goods = discount[i]
        buyable[goods] = buyable.get(goods, 0) + 1
    
    for i in range(len(discount) - 9):
        # 할인 품목과 위시리스트가 일치하는지 확인
        isAble = True
        for goods_name, amount in want_number.items():
            if goods_name not in buyable:
                isAble = False
                break
            if amount > buyable[goods_name]:
                isAble = False
                break
        if isAble:
            answer += 1
        # 최좌측 품목 제외
        most_left_goods = discount[i]
        buyable[most_left_goods] -= 1
        # 최우측 품목 추가
        if i+10 < len(discount):
            most_right_goods = discount[i+10]
            buyable[most_right_goods] = buyable.get(most_right_goods, 0) + 1
        
    return answer