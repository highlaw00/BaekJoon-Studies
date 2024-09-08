def get_number(i, j):
    if (j >= i): return j+1
    else: return i+1

def solution(n, left, right):
    answer = []
    
    left_i, left_j = left // n, left % n
    right_i, right_j = right // n, right % n
    
#     # left_i번째 행 삽입
#     for i in range(left_j, n):
#         answer.append(get_number(left_i, i))
    
#     # left_i ~ right_i 사이 행 삽입
#     for i in range(left_i+1, right_i):
#         for j in range(n):
#             answer.append(get_number(i, j))
    
#     # right_i번재 행 삽입
#     for i in range(right_j+1):
#         answer.append(get_number(right_i, i))
        
    for i in range(left_i, right_i+1):
        for j in range(n):
            if i == left_i and j < left_j:
                continue
            if i == right_i and j > right_j:
                continue
            answer.append(get_number(i,j))
    
    return answer