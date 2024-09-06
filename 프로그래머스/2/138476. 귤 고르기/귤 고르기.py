def solution(k, tangerine):
    answer = 0
    
    tangerine_map = dict()
    for size in tangerine:
        if size in tangerine_map:
            tangerine_map[size] += 1
        else:
            tangerine_map[size] = 1
    
    desc_tangerine = sorted(list(tangerine_map.values()), key = lambda x: -x)
    current_tangerine_cnt = 0
    
    while current_tangerine_cnt < k:
        current_tangerine_cnt += desc_tangerine[answer]
        answer += 1
    
    return answer