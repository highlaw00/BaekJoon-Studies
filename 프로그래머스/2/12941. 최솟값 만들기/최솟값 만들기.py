import heapq

def solution(A,B):
    answer = 0

    min_heap = []
    max_heap = []
    
    for elem in A:
        heapq.heappush(min_heap, elem)
    
    for elem in B:
        heapq.heappush(max_heap, -elem)
        
    while min_heap:
        min_val = heapq.heappop(min_heap)
        max_val = -heapq.heappop(max_heap)
        answer += min_val * max_val

    return answer