def solution(n, words):
    answer = [0, 0]
    turn = 0
    used = set()
    
    before_word = None
    
    for i, current_word in enumerate(words):
        current_player = i % n + 1;
        if current_player == 1:
            turn += 1
            
        # 이전 단어와 이어지지 않는 경우
        if before_word != None and before_word[-1] != current_word[0]:
            answer[0] = current_player
            answer[1] = turn
            break
        
        # 이미 사용한 단어인 경우
        if current_word in used:
            answer[0] = current_player
            answer[1] = turn
            break
        
        # 처음 사용한 경우
        used.add(current_word)
        before_word = current_word

    return answer