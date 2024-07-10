def is_solution(citations, h):
    over_citated = 0
    for citation in citations:
        if citation >= h:
            over_citated += 1
    if over_citated >= h:
        return True
    return False
    
def solution(citations):
    left = 0
    right = 10000
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        # h-index 만족하는지 확인
        result = is_solution(citations, mid)
        # h-index를 만족한다면 최적의 h는 [mid+1, right]에 존재
        if result:
            answer = mid
            left = mid + 1
        # h-index를 불만족하는 경우 최적 h는 [left, mid-1]에 존재
        else:
            right = mid - 1
            
    return answer