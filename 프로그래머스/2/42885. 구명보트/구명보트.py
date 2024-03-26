def solution(people, limit):
    n = len(people)
    # 정렬
    people.sort(key=lambda x: -x)
    
    left, right = 0, n-1
    answer = 0
    
    while left <= right:
        # 사람이 한 명 남은 경우
        if left == right:
            answer += 1
            break
        # 두 사람의 합이 limit을 초과하는 경우: 가장 무거운 사람을 혼자 태우고 왼쪽을 한칸 이동
        if people[left] + people[right] > limit:
            answer += 1
            left += 1
        # 두 사람의 합이 limit 이하인 경우: 둘 다 태우고 왼쪽과 오른쪽 모두 이동
        else:
            answer += 1
            left += 1
            right -= 1
    
    return answer