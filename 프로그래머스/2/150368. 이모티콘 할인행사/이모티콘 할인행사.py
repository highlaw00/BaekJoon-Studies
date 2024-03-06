ratios = [10, 20, 30, 40]
answer = [0, 0]

def back(candidates, cnt, users, emoticons):
    global ratios, answer
    # base case
    if cnt == len(emoticons):
        service_users = 0
        total_sales = 0
        for (ratio, price_limit) in users:
            summation = 0
            for i in range(len(candidates)):
                candidate_ratio = candidates[i]
                # 이모티콘 할인율이 더 큰 경우 -> 구매
                if ratio <= candidate_ratio:
                    summation += int(emoticons[i] * (100 - candidate_ratio) / 100)
            if summation >= price_limit:
                service_users += 1
            else:
                total_sales += summation
        
        if service_users > answer[0]:
            answer[0], answer[1] = service_users, total_sales
        elif service_users == answer[0] and total_sales > answer[1]:
            answer[1] = total_sales
        
        return
    
    for i in range(len(ratios)):
        candidates.append(ratios[i])
        back(candidates, cnt+1, users, emoticons)
        candidates.pop()
    
def solution(users, emoticons):
    candidates = []
    back(candidates, 0, users, emoticons)
    
    return answer