# A, B에게는 각 0~9까지의 10장의 카드가 주어진다. 순서는 무작위
# 한 라운드 = A, B 각각이 늘어놓은 카드를 뒤집어 숫자를 확인
# 총 10라운드이며 각 라운드에서 공개된 숫자가 더 큰 사람이 이김
# 승자에게는 3점의 승점이, 패자에게는 0점 비길 경우 1점이 주어짐

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ascr = 0
bscr = 0
draw_cnt = 0
last_winner = ''

for i in range(10):
    if a[i] > b[i]:
        ascr += 3
        last_winner = 'A'
    elif a[i] < b[i]:
        bscr += 3
        last_winner = 'B'
    else:
        ascr += 1
        bscr += 1
        draw_cnt += 1

print(ascr, bscr)
if ascr > bscr:
    print('A')
elif ascr < bscr:
    print('B')
else:
    if draw_cnt == 10:
        print('D')
    else:
        print(last_winner)