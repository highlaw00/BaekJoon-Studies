def back(cnt, stack, arr, m):
    if cnt == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(len(arr)):
        num = arr[i]
        stack.append(num)
        back(cnt+1, stack, arr, m)
        stack.pop()

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
back(0, [], arr, m)