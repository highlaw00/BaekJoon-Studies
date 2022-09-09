n, m = map(int, input().split())
array = list(map(int, input().split()))

sum_final = 0
gap_final = abs(m - (array[0] + array[1] + array[2]))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = array[i] + array[j] + array[k]
            gap = abs(m - sum)
            if (gap_final > gap and (sum_final < sum and sum <= m)):
                sum_final = sum
                gap_fianl = gap

print(sum_final)
