import sys
answer = 0

# 파라미터. k: 다음 인덱스
def back(stack, remain_fatig, dungeons):
    global answer
    answer = max(answer, len(stack))
    # base case: 더 이상 탐험할 수 있는 던전이 없는 경우
    if len(stack) >= len(dungeons):
        return
    
    for i in range(len(dungeons)):
        if i in stack: 
            continue
        
        need_fatig, consum_fatig = dungeons[i]
        if (remain_fatig >= need_fatig):
            stack.append(i)
            back(stack, remain_fatig-consum_fatig, dungeons)
            stack.pop()
    

def solution(k, dungeons):
    global answer
    back([], k, dungeons)
    return answer