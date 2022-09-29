n = int(input())

for _ in range(n):
    first, second = map(str, input().split())
    dist_list = []
    for i in range(len(first)):
        if first[i] > second[i]:
            # 두 번째 단어의 문자가 사전적으로 작을 경우
            dist = ord(second[i]) - ord(first[i]) + 26
        else:
            dist = ord(second[i]) - ord(first[i])
        dist_list.append(dist)
    print('Distances: ', end='')
    for w in dist_list:
        print(w, end=' ')
    print()
