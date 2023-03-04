n = int(input())

scores = [input().split() for _ in range(n)]

scores.sort(key=lambda p: [-int(p[1]), int(p[2]), -int(p[3]), p[0]])

for score in scores:
    print(score[0])
