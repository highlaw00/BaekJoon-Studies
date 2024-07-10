def solution(n, lost, reserve):
    remain_clothes = [0 for i in range(n+2)]
    for i in range(1, n+1):
        remain_clothe = 1
        if i in lost:
            remain_clothe -= 1
        if i in reserve:
            remain_clothe += 1
        remain_clothes[i] = remain_clothe
    
    # 앞사람에게 먼저 빌리고 뒷사람에게 나중에 빌리는 방법
    remain_clothes_cand1 = [remain_clothes[i] for i in range(n+2)]
    # # 뒷사람에게 먼저 빌리고 앞사람에게 나중에 빌리는 방법
    # remain_clothes_cand2 = [remain_clothes[i] for i in range(n+2)]
    
    # 앞사람에게 빌리고 없으면 뒷사람에게 빌리기
    for i in range(1, n+1):
        if remain_clothes_cand1[i] >= 1: continue
        if remain_clothes_cand1[i-1] >= 2:
            remain_clothes_cand1[i-1] -= 1
            remain_clothes_cand1[i] += 1
        elif remain_clothes_cand1[i+1] >= 2:
            remain_clothes_cand1[i+1] -= 1
            remain_clothes_cand1[i] += 1
    
#     for i in range(1, n+1):
#         if remain_clothes_cand2[i+1] >= 2:
#             remain_clothes_cand2[i+1] -= 1
#             remain_clothes_cand2[i] += 1
#         elif remain_clothes_cand2[i-1] >= 2:
#             remain_clothes_cand2[i-1] -= 1
#             remain_clothes_cand2[i] += 1
    
    answer_cand1 = 0
    # answer_cand2 = 0
    for remain_clothe in remain_clothes_cand1:
        if remain_clothe >= 1: answer_cand1 += 1
    # for remain_clothe in remain_clothes_cand2:
    #     if remain_clothe >= 1: answer_cand2 += 1    
    
    return answer_cand1