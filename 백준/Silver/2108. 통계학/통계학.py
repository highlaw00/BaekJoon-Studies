import sys
input = sys.stdin.readline

n = int(input())
l = []
d = {i: 0 for i in range(-4000, 4001)}
sum_ans = 0
for _ in range(n):
    x = int(input())
    sum_ans += x
    d[x] += 1
    l.append(x)

l.sort()
min_ans = l[0]
max_ans = l[-1]
range_ans = max_ans - min_ans
mid_ans = l[n//2]
freq_val = max(d.values())
candidates = []
for k, v in d.items():
    if v == freq_val:
        candidates.append(k)
if len(candidates) >= 2:
    freq_ans = candidates[1]
else:
    freq_ans = candidates[0]

print(round(sum_ans / n))
print(mid_ans)
print(freq_ans)
print(range_ans)
