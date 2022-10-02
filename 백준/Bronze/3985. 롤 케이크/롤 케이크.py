l = int(input())
cake = [-1 for _ in range(l)]
n = int(input())
max_gap = 0 # k - p + 1의 최대값
p_max_idx = 0 # 예상
prev = 0
cnt = 0
max_cnt = 0
r_max_idx = 0 # 실제

for i in range(n):
    p, k = map(int,input().split())
    gap = k - p + 1
    if gap > max_gap: 
        max_gap = gap
        p_max_idx = i + 1
    for j in range(p-1,k):
        if cake[j] == -1:
            cake[j] = i + 1

for i in range(l):
    if cake[i] != -1:
        if prev == 0:
            # 첫 원소일 때
            prev = cake[i]
            cnt += 1
        elif prev == cake[i]:
            # 이전 원소랑 같을 때
            cnt += 1
        else:
            # 이전 원소랑 다를 때
            prev = cake[i]
            cnt = 1
    else: continue
    if cnt > max_cnt:
        max_cnt = cnt
        r_max_idx = prev

print(p_max_idx)
print(r_max_idx)
        