sheet = [0 for _ in range(1_000_001)]
curr_idx = 1
nums = [i for i in range(10)]
visited = [False for _ in range(10)]

def back(cnt, maximum_len, array):
    global sheet, nums, visited, curr_idx
    if cnt == maximum_len and curr_idx <= 1_000_000:
        summation = 0
        curr_place = 10 ** (maximum_len - 1)
        for num in array:
            summation += curr_place * num
            curr_place = curr_place // 10
        sheet[curr_idx] = summation
        curr_idx += 1
        return

    for i in range(10):
        if cnt == 0 and i == 0:
            continue
        if visited[i]: continue
        array.append(i)
        visited[i] = True
        back(cnt + 1, maximum_len, array)
        visited[i] = False
        array.pop()

for i in range(1, 11):
    if curr_idx > 1_000_000: break
    back(0, i, [])

while True:
    n = int(input())
    if n == 0:
        break
    print(sheet[n])