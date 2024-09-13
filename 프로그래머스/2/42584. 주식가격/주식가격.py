def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i, price in enumerate(prices):
        while stack and stack[-1]['price'] > price:
            top_index = stack[-1]['index']
            answer[top_index] = i - top_index
            stack.pop()
        stack.append({'index': i, 'price': price})
    
    # 떨어지지 않은 주식 가격에 대해 갱신
    while stack:
        top_index = stack[-1]['index']
        answer[top_index] = len(prices) - 1 - top_index
        stack.pop()
    
    return answer