def is_avail_skill_tree(skill_order, skill_tree):
    ret_val = 1
    # 스킬 순서에 포함되는 스킬 기록
    skill_map = set()
    for skill in skill_order:
        skill_map.add(skill)
        
    skill_idx = 0
    for current_skill in skill_tree:
        # 스킬 순서에 포함되는 스킬이라면, 순서를 지켜야 됨
        if current_skill in skill_map:
            # 순서를 지킨 경우
            if skill_order[skill_idx] == current_skill:
                skill_idx += 1
            # 순서를 지키지 않은 경우
            else:
                ret_val = 0
                break
    
    return ret_val
                
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        # 스킬 트리 적합도 판단
        answer += is_avail_skill_tree(skill, skill_tree)
    
    return answer