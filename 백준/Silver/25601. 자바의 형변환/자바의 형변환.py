from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 클래스 관계 정보 주어짐
# Map에 클래스의 관계를 저장
d = dict()
for _ in range(n-1):
    # B가 부모, A가 자식
    a, b = input().rstrip().split()
    d[a] = b
    
o1, o2 = input().rstrip().split()

ans = 0
# o1을 자식이라고 보고 o2를 탐색합니다.
q = deque()

q.append(o1)
while q:
    curr_c = q.popleft()
    if curr_c in d:
        child = d[curr_c]
        if child == o2:
            ans = 1
            break
        q.append(child)

q = deque()

q.append(o2)
while q:
    curr_c = q.popleft()
    if curr_c in d:
        child = d[curr_c]
        if child == o1:
            ans = 1
            break
        q.append(child)

print(ans)
