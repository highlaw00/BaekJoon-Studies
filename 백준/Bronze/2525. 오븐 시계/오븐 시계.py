a, b = map(int, input().split())
c = int(input())

hour, minutes = c // 60, c % 60
ans_minutes = (b + minutes) % 60
ans_hour = (a + hour) % 24
ans_hour = (ans_hour + (b + minutes) // 60) % 24

print(ans_hour, ans_minutes)