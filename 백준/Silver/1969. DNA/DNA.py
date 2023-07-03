# 4가지의 뉴클레오티드 A C G T
# Hamming 거리 = 두 DNA를 비교했을 때 각 위치의 뉴클오티드 문자가 다른 것의 개수

# N개의 길이 M인 DNA s1, s2, ..., sn이 주어졌을 때,
# Hamming 거리가 가장 작은 DNA인 s를 구하라.
# s1과 s의 Hamming 거리는 모든 문자열을 확인하여 다른것의 개수를 확인하여 구함.
# 그렇다면 s는 s1,s2,...,sn 모두를 확인하여 각 자리마다 등장횟수가 가장 많은 문자로 이뤄질 것임.

# n,m 입력
# n개의 dna 입력
# n개의 dna를 기반으로 max_dna와 hamming distance를 출력

n, m = map(int, input().split())

dnas = []
ans = ''
dist = 0

for i in range(n):
    dna = input()
    dnas.append(dna)

# n개의 dna를 기반으로 max_dna 구하기
# m번동안 루프를 돌며 n개의 dna를 확인합니다.
for i in range(m):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    max = 0
    max_alpha = 'T'
    for j in range(n):
        curr_dna = dnas[j]
        char = curr_dna[i]
        dic[char] += 1

    # 가장 많이 나온 뉴클레오티드를 구합니다.
    for item in dic.items():
        key, value = item[0], item[1]
        if value > max:
            max_alpha, max = key, value
        elif value == max and key < max_alpha:
            max_alpha = key

    ans += max_alpha

    # Hamming 거리를 구합니다.
    # max_alpha와 key값이 다른 value를 모조리 더하면 됩니다.
    for item in dic.items():
        key, value = item[0], item[1]
        if key != max_alpha:
            dist += value

print(ans)
print(dist)
