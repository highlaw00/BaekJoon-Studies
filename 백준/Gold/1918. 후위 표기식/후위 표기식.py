line = input()
stack = []
ans = ""
sign_info = [[0, 0] for _ in range(len(line))]

# 우선순위 선정을 위해 sign_info를 초기화
bracket_cnt = 0
for i, ch in enumerate(line):
    if ch == '(':
        bracket_cnt += 1
    elif ch == ')':
        bracket_cnt -= 1
    elif ch in ('+', '-', '*', '/'):
        sign_info[i][0] = bracket_cnt
        sign_info[i][1] = 1 if ch in ('*', '/') else 0

# 문자열을 순회하며 다음과 같이 동작합니다.
# 만약 문자를 만나면 그대로 정답에 append합니다.
# 만약 (, )를 만나면 생략합니다.
# 만약 연산자를 만나면 다음과 같이 행동합니다.
# -> 스택이 비어있다면 스택에 삽입합니다.
# -> 만약 스택이 비지않았으면 우선순위를 비교하고 top의 우선순위가 더 높으면 대기. 동일하거나 낮으면 출력

for i, ch in enumerate(line):
    if ch in ('(', ')'):
        continue
    if ch in ('+', '-', '*', '/'):
        curr_sign = ch
        curr_priority, curr_sign_priority = sign_info[i]
        if not stack:
            stack.append((curr_sign, curr_priority, curr_sign_priority))
            continue
        top = stack[-1]
        top_sign, top_priority, top_sign_priority = top

        while top_priority > curr_priority or (top_priority == curr_priority and top_sign_priority >= curr_sign_priority):
            ans += top_sign
            stack.pop()
            if stack:
                top_sign, top_priority, top_sign_priority = stack[-1]
            else:
                break
        stack.append((curr_sign, curr_priority, curr_sign_priority))
    else:
        ans += ch

while stack:
    top_sign, _, _ = stack.pop()
    ans += top_sign

print(ans)
