import sys
input = sys.stdin.readline

n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
stack = []
nge = [-1 for _ in range(n)]
for i in range(n-1, -1, -1):
    # stack이 비어있다면 -1 & push
    if not stack:
        stack.append(A[i])
        continue

    while stack:
        # stack의 top이 현재 숫자보다 작거나 같으면 pop
        # pop한 후 stack이 비게 되면 push하고 다음으로
        if stack[-1] <= A[i]:
            stack.pop()
            if not stack:
                stack.append(A[i])
                break
        # stack의 top이 현재 숫자보다 크다면 nge에 해당 숫자 기입 및 push, break
        else:
            nge[i] = stack[-1]
            stack.append(A[i])
            break

print(' '.join(map(str, nge)))
