n = int(input())

for i in range(1, n + 1):
    for j in range(n - i):
        print(end=" ")
    for k in range(2 * i - 1):
        print(end="*")
    print()

# 총 줄의 개수는 n-1번이고
# 각 줄의 별 개수는 2n - (2i) -1개
# 각 줄의 공백 개수는 i개

for i in range(1, n):
    for j in range(i):
        print(end=" ")
    for k in range(2 * n - 2 * i - 1):
        print(end="*")
    print()
