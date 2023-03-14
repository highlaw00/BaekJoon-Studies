n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    # t1, t2 한 쌍씩 빼본다
    temp = arr[0:i] + arr[i + 1 : n]
    times = [False for _ in range(1000)]
    for elem in temp:
        for j in range(elem[0], elem[1]):
            times[j] = True
    # t1, t2 한 쌍을 뺐을 때 가장 긴 시간을 구한다
    cnt = 0
    for time in times:
        if time:
            cnt += 1
        if cnt >= ans:
            ans = cnt

print(ans)
