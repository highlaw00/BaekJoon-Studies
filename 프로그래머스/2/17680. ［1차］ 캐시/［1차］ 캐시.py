import sys 

def check_cache(caches, city):
    idx = -1
    for i, cache in enumerate(caches):
        # Hit
        if len(cache) != 0 and cache[0] == city:
            idx = i
            break
    return idx

def swap(caches, city, seq):
    # 빈 공간 확인
    for i, cache in enumerate(caches):
        # 빈 공간 존재
        if len(cache) == 0:
            caches[i] = [city, seq]
            return
    
    # 빈 공간 없음
    # LRU 방식으로 교체 - seq값이 가장 작은것을 찾아야함
    lru_idx = -1
    lru_val = sys.maxsize
    for i, cache in enumerate(caches):
        if cache[1] < lru_val:
            lru_val = cache[1]
            lru_idx = i
    
    caches[lru_idx] = [city, seq]

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i, city in enumerate(cities):
        cities[i] = city.lower()
    
    caches = [[] for _ in range(cacheSize)]
    
    for seq, city in enumerate(cities):
        idx = check_cache(caches, city)
        # 캐시 히트
        if idx != -1:
            # 참조 시점 기록
            caches[idx][1] = seq
            answer += 1
        # 캐시 미스
        else:
            # LRU 방식으로 교체
            swap(caches, city, seq)
            answer += 5
        
    return answer