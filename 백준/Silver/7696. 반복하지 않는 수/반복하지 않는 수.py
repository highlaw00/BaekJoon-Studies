from itertools import permutations, chain
import sys

# permutation을 list로 안바꾸고 해봅시다...

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cheat_sheet = []
unit = 0
flag = True

while flag:
    unit += 1
    candidates = permutations(arr, unit)
    last_idx = 0

    # 순열에서 0으로 시작하는거 다 거르기
    for candidate in candidates:
        if candidate[0] == 0:
            continue
        new_candidate = ''.join(map(str, candidate))
        cheat_sheet.append(int(new_candidate))
        if len(cheat_sheet) >= 1000000:
            flag = False
            break

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(cheat_sheet[n-1])
