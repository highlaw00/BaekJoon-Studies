def solution(dirs):
    answer = 0
    
    mapper = {
        'U': (1, 0),
        'D': (-1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    y, x = 0, 0
    visited = set()
    
    for dir in dirs:
        dy, dx = mapper[dir]
        ny, nx = y + dy, x + dx
        # 경계선 탈출 여부 확인
        if ny < -5 or nx < -5 or ny > 5 or nx > 5:
            continue
        route = (y, x, ny, nx)
        alt_route = (ny, nx, y, x)
        # 새롭게 방문하는 길인지 확인
        if route not in visited and alt_route not in visited:
            visited.add(route)
            visited.add(alt_route)
            answer += 1
        # 캐릭터 이동
        y, x = ny, nx
    
    return answer