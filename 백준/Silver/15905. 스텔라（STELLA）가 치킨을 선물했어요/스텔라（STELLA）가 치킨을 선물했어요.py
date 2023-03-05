# 학생 수 N 받음
n = int(input())

# 학생의 푼 문제와 패널티 점수 리스트의 원소로서 받기
grade = [list(map(int, input().split())) for _ in range(n)]

# 1. 푼 문제를 기준으로 내림차순 정렬
# 2. 패널티 점수를 기준으로 오름차순 정렬
grade.sort(key=lambda e: [-e[0], e[1]])

# 전체 학생에서 5등 추출, 5등과 푼 문제의 수가 같은 학생의 수 출력
fifth = grade[4]
ans = 0
for i in range(5, n):
    if grade[i][0] == fifth[0]:
        ans += 1
    elif grade[i][0] != fifth[0]:
        break
print(ans)
