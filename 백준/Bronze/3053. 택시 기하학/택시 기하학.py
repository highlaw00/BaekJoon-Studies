import math
# 유클리드 기하학에서 원의 넓이: pi * r * r
# 택시 기하학에서 원의 넓이: 2 * r * r

rad = int(input())

print('{0:.6f}'.format(math.pi * rad * rad))
print('{0:.6f}'.format(2 * rad * rad))