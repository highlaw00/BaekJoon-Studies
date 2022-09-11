curr, target = map(int,input().split())
n = int(input())
minimum = abs(curr - target)
# 1번 버튼이나 2번 버튼만 눌렀을 때 횟수가 최빈값이 되도록 세팅해준다.

for i in range(n):
    # 주파수를 누르면 바로 건너뛰기 때문에 이전 버튼의 정보를 저장할 필요가 없다.
    tmp = int(input())
    # tmp 버튼으로 이동 후 target까지의 거리를 현재 min과 비교해준다.
    tmp_dist = abs(target - tmp)
    if (tmp_dist < minimum):
        minimum = abs(target - tmp) + 1
        # 새로운 minimum 값은 n번째 버튼 누름(1) + target까지 1번 버튼이나 2번 버튼 누름(abs(target-tmp))
    else:
        continue    
    
print(minimum)