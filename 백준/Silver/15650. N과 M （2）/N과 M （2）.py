def back(cnt, k, stack, arr, m):
    if cnt == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(k, len(arr)):
        num = arr[i]
        if num in stack: 
            continue
        stack.append(num)
        back(cnt+1, i+1, stack, arr, m)
        stack.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
back(0, 0, [], arr, m)