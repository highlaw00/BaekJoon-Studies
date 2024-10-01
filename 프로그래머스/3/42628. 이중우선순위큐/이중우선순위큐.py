import heapq as hq
import sys

def solution(operations):
    answer = [-sys.maxsize, sys.maxsize]
    # 큐의 전체 상황을 조회할 수 있는 Dictionary 선언
    brief = dict()
    max_heap = []
    min_heap = []
    
    for op in operations:
        cmd, x = op.split()
        x = int(x)
        if cmd == 'I':
            brief[x] = brief.get(x, 0) + 1
            hq.heappush(max_heap, -x)
            hq.heappush(min_heap, x)
        # 최대값 삭제
        elif x == 1:
            # Max heap에서 삭제. 만약, 이미 삭제되었다면 무시
            while max_heap:
                num = -hq.heappop(max_heap)
                if brief[num] == 0:
                    continue
                # 힙에서 뺀 뒤에는 큐 상황 갱신
                brief[num] -= 1
                break            
        # 최소값 삭제
        else:
            while min_heap:
                num = hq.heappop(min_heap)
                if brief[num] == 0:
                    continue
                brief[num] -= 1
                break
    
    empty_cnt = 0
    for k, v in brief.items():
        if v == 0:
            empty_cnt += 1
            continue
        answer[0] = max(answer[0], k)
        answer[1] = min(answer[1], k)
    
    if empty_cnt == len(brief):
        answer = [0, 0]
        
    return answer