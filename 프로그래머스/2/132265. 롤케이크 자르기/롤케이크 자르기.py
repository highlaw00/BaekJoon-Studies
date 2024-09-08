def solution(topping):
    answer = 0
    
    n = len(topping)
    prefix = [0 for _ in range(n)]
    suffix = [0 for _ in range(n)]
    
    # prefix 채우기
    tasted = set()
    for i in range(n):
        curr_topping = topping[i]
        tasted.add(curr_topping)
        prefix[i] = len(tasted)
    
    # suffix 채우기
    tasted = set()
    for i in range(n-1, -1, -1):
        curr_topping = topping[i]
        tasted.add(curr_topping)
        suffix[i] = len(tasted)
    
    for i in range(n-1):
        if prefix[i] == suffix[i+1]:
            answer += 1
    
    return answer