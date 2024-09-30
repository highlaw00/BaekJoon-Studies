def solution(participant, completion):
    answer = ''
    completion_map = dict()
    for single_participant in participant:
        completion_map[single_participant] = completion_map.get(single_participant, 0) + 1
    
    for single_completion in completion:
        completion_map[single_completion] -= 1
    
    for name, cnt in completion_map.items():
        if cnt > 0:
            answer = name
            break
    
    return answer