def solution(numbers):
    dp = [-1 for _ in range(len(numbers))]
    
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] < numbers[i+1]:
            dp[i] = numbers[i+1]
            continue
        for j in range(i+1, len(numbers)):
            if dp[j] > numbers[i]:
                dp[i] = dp[j]
                break
            if dp[j] == -1 and numbers[i] >= numbers[j]:
                break
    
    return dp