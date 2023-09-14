import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    state_map = dict()

    for _ in range(k):
        cmd, n = input().rstrip().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            state_map[n] = state_map.get(n, 0) + 1
        else:
            # 최대 힙에서 삭제
            if n == 1:
                while max_heap:
                    root = -heapq.heappop(max_heap)
                    if state_map[root] != 0:
                        state_map[root] -= 1
                        break
            else:
                while min_heap:
                    root = heapq.heappop(min_heap)
                    if state_map[root] != 0:
                        state_map[root] -= 1
                        break

    # 최소 힙 남은 값 확인
    while min_heap:
        min_val = min_heap[0]
        if state_map[min_val] != 0:
            break
        else:
            heapq.heappop(min_heap)

    # 최대 힙 남은 값 확인
    while max_heap:
        max_val = -max_heap[0]
        if state_map[max_val] != 0:
            break
        else:
            heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(max_val, min_val)
