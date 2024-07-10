import heapq
from collections import deque

def solution(priorities, location):
    # 우선순위를 우선순위 큐에 삽입, max heap
    pq = []
    for priority in priorities:
        heapq.heappush(pq, -priority)
    
    # 프로세스 별 우선순위를 기록
    process_infos = dict()
    for idx, priority in enumerate(priorities):
        process_infos[idx] = priority
    
    # 큐 선언
    queue = deque()
    for i in range(len(priorities)): queue.append(i)
    
    # 큐를 순회하며 특정 프로세스가 수행되는 시점 반환
    answer = 0
    cnt = 1
    while queue:
        curr_proc_idx = queue.popleft()
        curr_proc_pri = process_infos[curr_proc_idx]
        # 현재 프로세스의 우선순위가 가장 높은 경우
        if curr_proc_pri == -pq[0]:
            heapq.heappop(pq)
            if curr_proc_idx == location:
                answer = cnt
                break
            else:
                cnt += 1
        # 현재 프로세스의 우선순위가 가장 높지 않은 경우
        else: 
            queue.append(curr_proc_idx)
    
    return answer