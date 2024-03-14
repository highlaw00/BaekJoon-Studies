import copy
n = int(input())
origin_infos = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def back(cnt, infos):
    global n, ans
    # 모든 계란을 던진 경우
    if cnt == n:
        broken_cnt = 0
        for info in infos:
            if info[0] <= 0:
                broken_cnt += 1
        ans = max(ans, broken_cnt)
        return
    
    # cnt 번째 계란이 이미 깨진 경우 skip
    if infos[cnt][0] <= 0:
        back(cnt + 1, infos)
        return
    
    broken_cnt = 0
    for i in range(n):
        # 자기 자신에게 던지는 경우는 스킵
        if i == cnt: continue
        # i번째 계란이 깨진 경우 skip
        if infos[i][0] <= 0: 
            broken_cnt += 1
            continue

        # cnt 번째 계란을 i번째 계란에게 던진다고 가정
        infos[i][0] -= infos[cnt][1]
        infos[cnt][0] -= infos[i][1]
        back(cnt + 1, infos)
        infos[i][0] += infos[cnt][1]
        infos[cnt][0] += infos[i][1]
    
    # 맞출 계란이 없는 경우 skip
    if broken_cnt == n - 1:
        back(cnt + 1, infos)

# 계란을 던지는 조합 경우의 수 뽑기
back(0, origin_infos)
print(ans)