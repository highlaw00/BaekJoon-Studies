import sys

n = int(input())
mat = [[0 for _ in range(n+1)]]
for _ in range(n):
    s = [0] + list(map(int, input().split()))
    mat.append(s)

selected = [False for _ in range(n+1)]
start_arr = []
score = sys.maxsize


def back(idx, cnt):
    if cnt == n // 2:
        # start 팀과 link 팀의 능력치 합산 구하기
        # start_arr에 존재하는 숫자들이 start 팀의 멤버들
        # link_arr에 존재하는 숫자들이 link 팀의 멤버들
        link_arr = []
        for i in range(1, n+1):
            if i not in start_arr:
                link_arr.append(i)
        start, link = 0, 0

        for i in range(n//2):
            for j in range(i+1, n//2):
                ss_ij = mat[start_arr[i]][start_arr[j]]
                ss_ji = mat[start_arr[j]][start_arr[i]]
                start += ss_ij + ss_ji

                ls_ij = mat[link_arr[i]][link_arr[j]]
                ls_ji = mat[link_arr[j]][link_arr[i]]
                link += ls_ij + ls_ji

        gap = abs(start-link)
        global score
        if gap < score:
            score = gap
        return
    for i in range(idx, n+1):
        start_arr.append(i)
        selected[i] = True
        back(i+1, cnt+1)
        start_arr.pop()
        selected[i] = False


back(1, 0)

print(score)
