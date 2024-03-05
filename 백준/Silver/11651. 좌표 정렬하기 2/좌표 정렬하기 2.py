import sys
input = sys.stdin.readline
n = int(input())
locations = []

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

locations.sort(key=lambda point: [point[1], point[0]])

for (x, y) in locations:
    print(x, y)