# 진실을 아는 사람들이 참가하는 파티 모두 순회
# 순회하는 파티에 참가한 모든 사람들을 진실을 아는 사람으로 변환
# 진실을 아는 사람들이 없는 파티만 count해서 정답 출력

# 큐를 선언
# 방문 배열 선언
# 큐에 진실을 아는 사람들을 하나씩 삽입
# 순회하면서 진실을 아는 사람으로 변한 진실을 모르는 사람을 큐에 삽입
# 큐가 빌때까지 반복 후 전체 순회 후 정답 출력

from collections import deque

n, m = map(int, input().split())
knows = list(map(int, input().split()))
know_n = knows[0]
knows = knows[1:]
# 파티 정보
parties = [set()]
participants = [set() for _ in range(n+1)]

for party_idx in range(1, m+1):
    # 파티 참가 인원 삽입
    party = set(list(map(int, input().split()))[1:])
    # 사람이 참가하고 있는 파티 인덱스 저장
    for p_idx in party:
        participants[p_idx].add(party_idx)
    parties.append(party)

visited = [0 for _ in range(n+1)]
q = deque()
# 큐에 진실을 아는 사람들 삽입
for know in knows:
    q.append(know)
    visited[know] = 1

while q:
    know = q.popleft()
    # 진실을 아는 사람이 참가하는 파티 전체 순회
    for participant in participants[know]:
        # 참가한 사람이 진실을 알지 않는다면
        # 진실을 알게 만들고 큐에 삽입
        party = parties[participant]
        for people in party:
            if not visited[people]:
                visited[people] = 1
                q.append(people)

ans = -1
# 이제 파티를 순회하면서 진실을 아는 사람이 없는 파티의 개수를 세줍니다
for party in parties:
    is_cheatable = True
    for participant in party:
        if visited[participant]:
            is_cheatable = False
            break
    if is_cheatable:
        ans += 1

print(ans)
