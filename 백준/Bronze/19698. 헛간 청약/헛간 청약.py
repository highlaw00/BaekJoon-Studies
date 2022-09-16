# 헛간은 W X H 크기의 직사각형
# 소 한 마리 당 L X L의 크기를 배정
# 최대한 몇 마리의 소들이 입주할 수 있는지 출력

n, w, h, l = map(int, input().split())

wmax = w // l
hmax = h // l

maxroom = wmax * hmax

if maxroom >= n:
    print(n)
else:
    print(maxroom)
