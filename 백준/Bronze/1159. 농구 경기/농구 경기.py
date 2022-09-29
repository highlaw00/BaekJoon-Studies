# 문자열이 입력이 되고, 문자열의 첫번째 글자가 5개 이상인 글자를 사전순으로 출력한다.

n = int(input())
D = dict()

for i in range(n):
    name = input()
    fname = name[0]
    if fname not in D:
        D[fname] = 1
    else:
        D[fname] += 1

l = []

for key in D:
    if D[key] >= 5:
        l.append(key)

if len(l) == 0:
    print('PREDAJA')
else:
    l.sort()
    for w in l:
        print(w, end='')