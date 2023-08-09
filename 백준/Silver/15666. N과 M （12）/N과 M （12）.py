n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
sheet = []
nums = set()


def back(cnt, idx):
    if cnt == m:
        if tuple(sheet) not in nums:
            print(' '.join(map(str, sheet)))
            nums.add(tuple(sheet))
        return
    for i in range(idx, n):
        sheet.append(A[i])
        back(cnt + 1, i)
        sheet.pop()


back(0, 0)
