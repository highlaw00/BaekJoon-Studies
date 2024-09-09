def solution(s):
    
    numbers = list(map(int, s.split()))
    min_val = min(numbers)
    max_val = max(numbers)
    
    return str(min_val) + " " + str(max_val)