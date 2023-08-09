# n개의 자연수와 자연수 m이 주어졌을 때 길이가 m인 수열을 모두 구하는 프로그램
# n개의 자연수 중에서 m개를 고른 수열
# 중복되는 수열을 여러번 출력하면 안됨

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
sheet = []
idx_sheet = []
nums = set()


def back(cnt):
    if cnt == m:
        if tuple(sheet) not in nums:
            print(' '.join(map(str, sheet)))
            nums.add(tuple(sheet))
        return
    for i in range(n):
        if idx_sheet and i in idx_sheet:
            continue
        idx_sheet.append(i)
        sheet.append(A[i])
        back(cnt+1)
        idx_sheet.pop()
        sheet.pop()


back(0)
