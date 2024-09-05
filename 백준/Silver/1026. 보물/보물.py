import heapq

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_heap = []
min_heap = []

for elem in A:
    heapq.heappush(min_heap, elem)

for elem in B:
    heapq.heappush(max_heap, -elem)

ans = 0
while max_heap:
    min_val = heapq.heappop(min_heap)
    max_val = -heapq.heappop(max_heap)
    ans += min_val * max_val

print(ans)