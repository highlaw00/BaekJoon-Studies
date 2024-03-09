def solution(data, col, row_begin, row_end):
    # row_begin, row_end = 1-index
    # 1 xor 1 => 0 / 1 xor 0 => 1 / 0 xor 0 => 0
    
    # 데이터 정렬 (col 번째 오름차순, PK 내림차순)
    data.sort(key=lambda x: [x[col-1], -x[0]])
    
    answer = 0
    # row_begin번째부터 row_end번째의 S_i 구해 XOR하기
    for i in range(row_begin - 1, row_end):
        temp_sum = 0
        for num in data[i]:
            temp_sum += num % (i + 1)
        answer = answer ^ temp_sum
        
    
    return answer