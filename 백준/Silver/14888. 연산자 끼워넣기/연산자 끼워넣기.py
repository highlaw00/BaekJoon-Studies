import sys
max_ans = -sys.maxsize
min_ans = sys.maxsize
n = int(input())

nums = list(map(int, input().split()))
# +, -, * , //
ops = list(map(int, input().split()))

# n-1개의 연산자를 고르고 그 값을 계산한다. (백트래킹)
def back(cnt, selected_ops):
    global n, nums, ops, min_ans, max_ans
    # cnt: 현재 고른 연산자의 개수
    
    # 연산자를 모두 선택한 경우
    if cnt == n-1:    
        result = nums[0]
        for i in range(len(selected_ops)):
            if selected_ops[i] == 0:
                result = result + nums[i+1]
            if selected_ops[i] == 1:
                result = result - nums[i+1]
            if selected_ops[i] == 2:
                result = result * nums[i+1]
            if selected_ops[i] == 3:
                if result < 0:
                    result = -(-result // nums[i+1])
                else:
                    result = result // nums[i+1]
        
        min_ans = min(min_ans, result)
        max_ans = max(max_ans, result)
        return
    
    for i in range(4):
        # 현재 연산자가 존재한다면 선택
        if ops[i] > 0:
            ops[i] -= 1
            selected_ops.append(i)
            back(cnt + 1, selected_ops)
            selected_ops.pop()
            ops[i] += 1

back(0, [])

print(max_ans)
print(min_ans)