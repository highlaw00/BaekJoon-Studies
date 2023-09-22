n = int(input())
m = int(input())
s = input()


def toggle(t):
    return 'O' if t == 'I' else 'I'


# 주어진 문자를 확인
target = 'I'
isFounded = False
ans = 0
acc = 0
for ch in s:
    # 아직까지 못찾은 상태
    if not isFounded:
        # 찾으려는 문자열과 일치
        if target == ch:
            # 타겟 토글 및 누적합 + 1
            acc += 1
            target = toggle(target)
        # 찾는데 실패
        else:
            if ch == 'I':
                acc = 1
                target = 'O'
            else:
                acc = 0
                target = 'I'
        # 이번 문자로 인해 찾게 됨
        if acc == 2*n + 1:
            isFounded = True
            ans += 1
    # 이미 찾은 상태
    else:
        # 찾으려는 문자와 일치('O', 'I')
        if target == ch:
            acc += 1
            target = toggle(target)
        # 찾으려는 문자가 아님
        # 이 경우, 타겟 변경 및 누적합 초기화 및 불리언 초기화
        else:
            isFounded = False
            if ch == 'I':
                acc = 1
                target = 'O'
            else:
                acc = 0
                target = 'I'
            continue
        # 'O', 'I'를 순차적으로 찾은 경우
        if acc % 2 == 1:
            ans += 1

print(ans)
