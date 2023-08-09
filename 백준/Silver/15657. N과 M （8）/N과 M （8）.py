# 길이가 m인 수열을 모두 구하라, n개의 자연수는 모두 다른 수
# n개의 자연수 중 m개를 고른 수열
# 같은 수를 여러번 골라도 됨
# 고른 수열은 비내림차순이어야 함
# 비내림차순이란 a1 <= a2 <= ... <= ak-1 <= ak를 만족하면 비내림차순

# 오름차순으로 리스트를 정렬한 뒤 백트래킹 하면 될 듯

n, m = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
sheet = []
nums = set()


def back(cnt, idx):
    # 기저 사례 삽입
    if cnt == m:
        if tuple(sheet) not in nums:
            print(' '.join(map(str, sheet)))
        return

    # 하나씩 뽑기
    for i in range(idx, n):
        sheet.append(A[i])
        back(cnt+1, i)
        sheet.pop()


back(0, 0)
