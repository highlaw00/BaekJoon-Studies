n = int(input())
D = dict()

for _ in range(n):
    s = input()
    if s not in D: D[s] = 1
    else: D[s] += 1

max_name = list(D.keys())[0]
max = list(D.values())[0]
ans = ''

for key in D:
    value = D[key]
    if value > max:
        max_name = key
        max = value
    elif value == max:
        if key < max_name:
            # 최대값이며 사전순으로 현재 최대값의 이름보다 빠를 때
            max_name = key
    
print(max_name)