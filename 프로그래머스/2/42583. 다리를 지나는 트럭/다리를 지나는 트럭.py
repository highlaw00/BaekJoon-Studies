from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_len = len(truck_weights)
    passed_truck_cnt = 0
    remain_truck_queue = deque(truck_weights)
    trucks_on_bridge = deque()
    current_bridge_weight = 0
    
    # 다리 위 트럭 정보: {location: X, weight: Y}
    
    while passed_truck_cnt < truck_len:
        # 1초 지남
        answer += 1
        
        # bridge 위에 존재하는 트럭 1칸씩 이동
        for truck in trucks_on_bridge:
            truck["location"] += 1
        
        # 끝까지 도달한 트럭 내보내기
        if len(trucks_on_bridge) >= 1 and trucks_on_bridge[0]["location"] > bridge_length:
            lefting_truck = trucks_on_bridge[0]
            current_bridge_weight -= lefting_truck["weight"]
            trucks_on_bridge.popleft()
            passed_truck_cnt += 1
            
        if remain_truck_queue:
            next_truck = remain_truck_queue[0]
        else:
            continue
        
        # bridge에 새로운 트럭이 올라올 수 있는지 확인
        if remain_truck_queue and len(trucks_on_bridge) <= bridge_length and current_bridge_weight + next_truck <= weight:
            # 다리 중량 추가
            current_bridge_weight += next_truck
            # 트럭이 새롭게 올라옴.
            trucks_on_bridge.append({"weight": next_truck, "location": 1})
            remain_truck_queue.popleft()
    
    return answer