n = int(input())

for i in range(1, n + 1):
    # n번째 줄에 n-i개의 공백을 찍는다.
    # n번째 줄에 2i-1개의 별을 찍는다.
    for j in range(n - i):
        print(end=" ")
    for k in range(2 * i - 1):
        print(end="*")
    print()