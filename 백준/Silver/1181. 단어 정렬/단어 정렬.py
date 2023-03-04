n = int(input())

arr = list({input() for _ in range(n)})

arr.sort(key=lambda word: [len(word), word])

for word in arr:
    print(word)
