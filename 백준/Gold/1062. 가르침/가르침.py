# 글자 k개를 어떻게 가르쳐야 최대한 많은 단어를 알 수 있게 만들까?
# 단어가 N개
# k개의 글자를 백트래킹 기법으로 완전 탐색 하는데,
# 그렇게 정한 k개의 글자로 읽을 수 있는 단어를 세줍니다.
# 단어의 개수가 가장 큰 경우를 출력하면 되는 문제

# 26개의 문자 중 k개의 문자를 집합에 삽입
# 전처리: N개의 단어에 대해서, 해당 단어가 보유하고 있는 알파벳의 종류를 집합에 삽입
# 총 N개의 집합이 생성됨
# k개의 문자를 모두 골랐으면, N개의 집합과 고른 문자들의 집합을 대조.
# 읽을 수 있다면(N개의 집합에 있는 모든 문자가 고른 문자들의 집합에 존재하는 경우) + 1
# N개의 집합 모두 대조해보고 ans 갱신

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
words_set = [set(input().rstrip()) for _ in range(n)]

# 처음부터 a,c,i,n,t 를 넣고 시작하기
sheet = set()
for char in ('a', 'c', 'i', 'n', 't'):
    sheet.add(char)

# 'a'부터 'z'까지 저장
alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ans = 0


def back(cnt, idx):
    # cnt: 현재 배운 글자의 수
    # idx: 배울 수 있는 글자 중 가장 낮은 인덱스

    # k보다 많이 배우는 경우 (k가 5보다 작은 경우)
    if cnt > k:
        return
    # 배운 글자 수가 k개
    if cnt == k:
        # 모든 단어 집합과 sheet 집합 비교
        readable_cnt = 0
        for i in range(n):
            word_set = words_set[i]
            flag = True
            for char in word_set:
                # 읽을 수 없음
                if char not in sheet:
                    flag = False
                    break
            if flag:
                readable_cnt += 1
        global ans
        ans = max(ans, readable_cnt)
        return
    # 알파벳 리스트에서 k개 고르기
    for i in range(idx, len(alphabets)):
        char = alphabets[i]
        # 이미 고른 경우 (a,c,i,n,t) continue
        if char in sheet:
            continue
        sheet.add(char)
        back(cnt+1, i+1)
        sheet.remove(char)


back(len(sheet), 0)

print(ans)
