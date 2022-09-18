n = int(input())
l = [int(input()) for _ in range(n)]
cnt = 0

while True:
    max_val = max(l)
    # 리스트 내 l[0]보다 큰 값이나 같은 값이 없는 경우 break해주면 된다!
    if l[0] == max_val:
        overlap_cnt = 0
        overlap_idx = 0
        for i in range(1, n):
            if l[i] == max_val:
                overlap_cnt += 1
                overlap_idx = i
        # l[0]이 가장 큰 값이면서 중복되는 값이 없는 경우 탈출!
        if overlap_cnt == 0:
            break
        # l[0]이 가장 큰 값이지만 중복되는 값이 있는 경우 중복되는 놈을 매수한다.
        else:
            l[overlap_idx] -= 1
            l[0] += 1
            cnt += 1
    # l[0]이 아직 가장 큰 값이 아닌 경우 가장 큰 놈을 찾아 매수한다.
    else:
        max_idx = l.index(max_val)
        l[max_idx] -= 1
        l[0] += 1
        cnt += 1
        
print(cnt)