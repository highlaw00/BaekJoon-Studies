def dec_to_bin(decimal):
    return bin(decimal)[2:]

def solution(s):
    answer = []
    transform_cnt = 0
    total_zero_cnt = 0
    
    while s != '1':
        zero_cnt = 0
        one_cnt = 0
        for ch in s:
            if ch == '0':
                zero_cnt += 1
        one_cnt = len(s) - zero_cnt
        new_s = dec_to_bin(one_cnt)
        
        total_zero_cnt += zero_cnt
        transform_cnt += 1
        
        s = new_s
    
    return [transform_cnt, total_zero_cnt]