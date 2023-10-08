n = int(input())
options = [0 for _ in range(n)]
short_cuts = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
short_cuts_indices = [-1 for _ in range(n)]

for i in range(n):
    option = input()
    options[i] = option

for i, option in enumerate(options):
    is_saved = False
    prev_ch = ' '
    # 각 문자열의 첫번째 글자만을 확인
    for j, ch in enumerate(option):
        ch = ch.upper()
        if prev_ch == ' ':
            # 첫번째 글자가 단축키로 지정 가능한 경우
            if not short_cuts[ch]:
                short_cuts[ch] = True
                short_cuts_indices[i] = j
                is_saved = True
                break
        prev_ch = ch

    if is_saved:
        continue

    for j, ch in enumerate(option):
        if ch == ' ':
            continue
        ch = ch.upper()
        if not short_cuts[ch]:
            short_cuts[ch] = True
            short_cuts_indices[i] = j
            break

for i, option in enumerate(options):
    short_cut_idx = short_cuts_indices[i]
    if short_cut_idx == -1:
        print(option)
        continue
    print(option[:short_cut_idx] +
          '[' + option[short_cut_idx] + ']' + option[short_cut_idx+1:])
