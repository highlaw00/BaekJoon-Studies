def back(cnt, stack, arr, m):
    # base condition
    if cnt == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(len(arr)):
        num = arr[i]
        if num in stack: continue
        stack.append(num)
        back(cnt+1, stack, arr, m)
        stack.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
back(0, [], arr, m)