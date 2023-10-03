import sys

s = []
ans = []
latest_right_ancestors = []

while True:
    line = sys.stdin.readline().rstrip()
    if line == '':
        break
    x = int(line)

    if not s:
        s.append(x)
        continue

    # top이 x보다 큰 경우 s의 좌측 자손
    if s[-1] > x:
        latest_right_ancestors.append(s[-1])
        s.append(x)
        continue

    # 우측 자식일 가능성이 존재하는 경우
    # 아직 최 우측 조상이 없는 경우
    if not latest_right_ancestors:
        s.append(x)
        continue
    # 최우측 조상값이 있을 때... x를 적절한 최우측 조상값에 껴야한다.
    # 최우측 조상보다 작다면? 현재 부모의 우측 자식
    # 최우측 조상보다 크다면? 최우측 조상의 우측 자식이거나 다음 최우측 조상의 우측 자식
    while latest_right_ancestors:
        # 최우측 조상보다 x가 작은 경우
        # 현재 부모의 우측 자식임
        if latest_right_ancestors[-1] > x:
            break
        # 최우측 조상보다 x가 큰 경우
        # 현재 부모가 최우측 조상이 될 때까지 ans에 포함
        while s[-1] != latest_right_ancestors[-1]:
            ans.append(s.pop())
        latest_right_ancestors.pop()
    s.append(x)

for i in range(len(s)):
    ans.append(s.pop())

for num in ans:
    print(num)
