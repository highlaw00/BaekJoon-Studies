def solution(s):
    # chunks = s.split()
    # for i, chunk in enumerate(chunks):
    #     chunks[i] = chunk.capitalize()
    # answer = ' '.join(chunks)
    isCapital = True
    answer = ''
    for i, ch in enumerate(s):
        if isCapital:
            if ch == ' ':
                answer += ch
            elif 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
                isCapital = False
                answer += ch.upper()
            else:
                # 알파벳이 아닌 문자가 첫번째 자리에 오는 경우
                isCapital = False
                answer += ch
        elif ch == ' ':
            isCapital = True
            answer += ch
        elif 'A' <= ch <= 'Z':
            answer += ch.lower()
        else:
            answer += ch
            
    return answer