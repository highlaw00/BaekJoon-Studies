# 가로 길이는 세로 길이가 될 수 있고, 세로 길이는 가로 길이가 될 수 있다.
# 가로 길이와 세로 길이의 최대값을 최소로 하는 값을 찾아야 함.

def solution(sizes):
    answer = 0
    h_max = 0
    w_max = 0
    
    for w, h in sizes:
        # 뒤집기 전 최대 넓이 구하기
        extent_unflipped = max(h_max, h) * max(w_max, w)
        # 뒤집은 후 최대 넓이 구하기
        extent_flipped = max(h_max, w) * max(w_max, h)
        
        if (extent_unflipped >= extent_flipped):
            h_max = max(h_max, w)
            w_max = max(w_max, h)
        else:
            h_max = max(h_max, h)
            w_max = max(w_max, w)
            
    return h_max * w_max