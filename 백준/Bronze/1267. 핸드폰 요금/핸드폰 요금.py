n = int(input())
l = list(input().split())

ysum = 0
msum = 0

for i in range(n):
    curr = int(l[i])
    ysum += (int(curr / 30) + 1) * 10
    msum += (int(curr / 60) + 1) * 15

if ysum > msum:
    print('M {}'.format(msum))
elif ysum < msum:
    print('Y {}'.format(ysum))
else:
    print('Y M {}'.format(ysum))
