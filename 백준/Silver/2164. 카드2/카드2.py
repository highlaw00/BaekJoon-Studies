from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])

while len(cards) > 1:
    # top 제거
    cards.popleft()
    # top을 bottom에 배치
    cards.append(cards.popleft())

print(cards[0])
