import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    left_small_cnt = 0
    right_small_cnt = 0
    left_big_cnt = 0
    right_big_cnt = 0

    is_balanced = True
    expected_brackets = []
    for ch in line:
        if ch == '(':
            left_small_cnt += 1
            expected_brackets.append(')')
        if ch == ')':
            right_small_cnt += 1
            if expected_brackets:
                if expected_brackets[-1] != ch:
                    is_balanced = False
                    break
                expected_brackets.pop()
        if ch == '[':
            left_big_cnt += 1
            expected_brackets.append(']')
        if ch == ']':
            right_big_cnt += 1
            if expected_brackets:
                if expected_brackets[-1] != ch:
                    is_balanced = False
                    break
                expected_brackets.pop()

        if right_small_cnt > left_small_cnt or right_big_cnt > left_big_cnt:
            is_balanced = False
            break

    if left_small_cnt != right_small_cnt or left_big_cnt != right_big_cnt:
        is_balanced = False

    if is_balanced:
        print('yes')
    else:
        print('no')
