answer = 0

def dfs(numbers, target, idx, current_sum):
    global answer
    if idx == len(numbers):
        if current_sum == target:
            answer += 1
        return
    
    current_num = numbers[idx]
    dfs(numbers, target, idx + 1, current_sum + current_num)
    dfs(numbers, target, idx + 1, current_sum - current_num)
    

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer