import math

ans_set = set()

def back(cnt, stack, string, selected_indices):
    global ans_set
    # 소수확인
    if stack:
        num = int(''.join(stack))
        isPrime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                isPrime = False
                break
        if num == 2 or num == 3:
            isPrime = True
        if num > 1 and isPrime:
            ans_set.add(num)
    
    if len(stack) >= len(string):
        return
    
    for i in range(len(string)):
        if i in selected_indices: 
            continue
        num = string[i]
        selected_indices.add(i)
        stack.append(num)
        back(i+1, stack, string, selected_indices)
        stack.pop()
        selected_indices.remove(i)
    
def solution(numbers):
    global ans_set
    
    back(0, [], numbers, set())
    
    # print(ans_set)
    
    return len(ans_set)