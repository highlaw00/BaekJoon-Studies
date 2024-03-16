is_self_num = [True for _ in range(10_001)]

def recursive_d(n):
    global is_self_num
    # n과 n의 각 자리수를 모두 더한 값을 return
    summation = n
    temp = n
    while temp != 0:
        summation += temp % 10
        temp = temp // 10
    if summation > 10_000: 
        return
    is_self_num[summation] = False
    recursive_d(summation)

for i in range(1, len(is_self_num)):
    if is_self_num[i]:
        print(i)
        recursive_d(i)