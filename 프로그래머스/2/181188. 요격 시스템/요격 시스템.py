def solution(targets):
    answer = 0
    bombs = []
    for id, bomb in enumerate(targets):
        s, e = bomb
        bombs.append((s, 1, id))
        bombs.append((e, -1, id))
    bombs.sort()
    is_exploded = [False for _ in range(len(targets))]
    met = []
    for bomb in bombs:
        x, w, id = bomb
        if w == 1:
            met.append(id)
        else:
            # 이미 요격된 미사일이라면 무시
            if is_exploded[id]: continue
            else:
                is_exploded[id] = True
                answer += 1
                while met:
                    id = met.pop()
                    is_exploded[id] = True

    return answer