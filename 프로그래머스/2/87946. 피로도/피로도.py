answer = 0

# parameter: 현재 방문 던전의 리스트, 남아있는 피로도
def back(visited, dungeons, remain_fatig):
    global answer
    answer = max(answer, len(visited))
    for idx, (min_req_fatig, consum_fatig) in enumerate(dungeons):
        if idx in visited: continue
        if remain_fatig >= min_req_fatig:
            visited.append(idx)
            remain_fatig -= consum_fatig
            back(visited, dungeons, remain_fatig)
            remain_fatig += consum_fatig
            visited.pop()

def solution(k, dungeons):
    global answer
    back([], dungeons, k)
    return answer