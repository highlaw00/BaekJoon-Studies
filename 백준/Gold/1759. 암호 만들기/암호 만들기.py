# 암호는 서로 다른 L개의 알파벳 소문자로 구성되며
# 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다
# 알파벳이 증가하는 순서로 배열되어 있어야 가능성있는 암호
# C개의 문자가 주어졌을 때 가능성 있는 모든 암호를 구하라

l, c = map(int, input().split())

chars = input().split()
chars.sort()

# c개의 알파벳을 선택하고, 그렇게 선택한 알파벳이 조건을 만족하는지 확인
# 증가하는 순서로 배열되어야하고, 중복되는것이 없다
# 백트래킹을 진행할 때, 미리 알파벳을 정렬하고 중복을 배제한다
sheet = []


def back(cnt, idx):
    if cnt == l:
        # 우선, 알파벳 내 한 개의 모음과 두 개의 자음이 존재하는지 확인
        vowel_cnt = 0
        cons_cnt = 0
        for char in sheet:
            if char in ('a', 'e', 'i', 'o', 'u'):
                vowel_cnt += 1
            else:
                cons_cnt += 1
        if vowel_cnt < 1 or cons_cnt < 2:
            return

        print(''.join(sheet))
    for i in range(idx, c):
        sheet.append(chars[i])
        back(cnt+1, i+1)
        sheet.pop()


back(0, 0)
